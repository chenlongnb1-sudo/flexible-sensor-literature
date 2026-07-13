#!/usr/bin/env python3
"""Local API and static server for the research-intelligence dashboard."""

from __future__ import annotations

import argparse
import json
import mimetypes
import subprocess
import sys
import threading
import urllib.parse
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path, PurePosixPath
from typing import Any

try:
    from .build_research_intelligence import MEMORY, ROOT, refresh_bundle
    from .research_store import StoreError, apply_decision, apply_proposal, git_sync
except ImportError:
    from build_research_intelligence import MEMORY, ROOT, refresh_bundle
    from research_store import StoreError, apply_decision, apply_proposal, git_sync


WEB_ROOT = (ROOT / "web").resolve()
DAILY_LOCK = threading.Lock()


class ResearchHandler(BaseHTTPRequestHandler):
    server_version = "ResearchIntelligence/1.0"

    def send_json(self, payload: Any, status: HTTPStatus = HTTPStatus.OK) -> None:
        raw = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(raw)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(raw)

    def read_json(self) -> dict[str, Any]:
        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError as error:
            raise StoreError("invalid content length") from error
        if length <= 0 or length > 128 * 1024:
            raise StoreError("invalid request body size")
        try:
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise StoreError("invalid JSON body") from error
        if not isinstance(payload, dict):
            raise StoreError("JSON body must be an object")
        return payload

    def do_GET(self) -> None:  # noqa: N802 - BaseHTTPRequestHandler interface
        path = urllib.parse.urlparse(self.path).path
        if path == "/api/health":
            self.send_json({"ok": True, "mode": "local-write", "service": self.server_version})
            return
        if path == "/api/bundle":
            self.send_json(refresh_bundle())
            return
        if path.startswith("/files/"):
            self.serve_research_file(path)
            return
        self.serve_static(path)

    def do_POST(self) -> None:  # noqa: N802 - BaseHTTPRequestHandler interface
        path = urllib.parse.urlparse(self.path).path
        try:
            if path == "/api/decisions":
                self.send_json(apply_decision(self.read_json()))
                return
            if path.startswith("/api/proposals/"):
                parts = [part for part in path.split("/") if part]
                if len(parts) != 4:
                    raise StoreError("invalid proposal endpoint")
                payload = self.read_json()
                self.send_json(apply_proposal(parts[2], parts[3], str(payload.get("note") or "")))
                return
            if path == "/api/sync":
                payload = self.read_json()
                message = str(payload.get("message") or "chore: sync research decisions")[:120]
                self.send_json({"ok": True, **git_sync(message)})
                return
            if path == "/api/run-daily":
                payload = self.read_json()
                self.run_daily(bool(payload.get("download_pdfs", True)))
                return
            self.send_json({"error": "not found"}, HTTPStatus.NOT_FOUND)
        except StoreError as error:
            self.send_json({"error": str(error)}, HTTPStatus.BAD_REQUEST)
        except subprocess.CalledProcessError as error:
            self.send_json(
                {"error": f"command failed: {' '.join(str(part) for part in error.cmd)}"},
                HTTPStatus.INTERNAL_SERVER_ERROR,
            )
        except Exception as error:  # noqa: BLE001 - convert server errors to JSON
            self.send_json(
                {"error": f"{type(error).__name__}: {error}"},
                HTTPStatus.INTERNAL_SERVER_ERROR,
            )

    def run_daily(self, download_pdfs: bool) -> None:
        if not DAILY_LOCK.acquire(blocking=False):
            self.send_json({"error": "daily pipeline is already running"}, HTTPStatus.CONFLICT)
            return
        try:
            command = [sys.executable, str(ROOT / "scripts" / "daily_literature_pipeline.py")]
            if not download_pdfs:
                command.append("--no-pdf")
            result = subprocess.run(
                command,
                cwd=ROOT,
                check=False,
                text=True,
                encoding="utf-8",
                errors="replace",
                capture_output=True,
                timeout=8 * 60,
            )
            status = HTTPStatus.OK if result.returncode == 0 else HTTPStatus.INTERNAL_SERVER_ERROR
            self.send_json(
                {
                    "ok": result.returncode == 0,
                    "stdout": result.stdout[-4000:],
                    "stderr": result.stderr[-4000:],
                    "bundle": refresh_bundle(),
                },
                status,
            )
        finally:
            DAILY_LOCK.release()

    def serve_static(self, request_path: str) -> None:
        relative = request_path.lstrip("/") or "index.html"
        candidate = (WEB_ROOT / relative).resolve()
        if WEB_ROOT not in candidate.parents and candidate != WEB_ROOT:
            self.send_error(HTTPStatus.FORBIDDEN)
            return
        if candidate.is_dir():
            candidate = candidate / "index.html"
        if not candidate.exists() or not candidate.is_file():
            self.send_error(HTTPStatus.NOT_FOUND)
            return
        raw = candidate.read_bytes()
        mime, _ = mimetypes.guess_type(candidate.name)
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", f"{mime or 'application/octet-stream'}; charset=utf-8")
        self.send_header("Content-Length", str(len(raw)))
        self.send_header(
            "Cache-Control",
            "no-store"
            if candidate.suffix in {".html", ".json", ".js", ".css", ".webmanifest"}
            else "public, max-age=3600",
        )
        self.end_headers()
        self.wfile.write(raw)

    def serve_research_file(self, request_path: str) -> None:
        relative = PurePosixPath(urllib.parse.unquote(request_path.removeprefix("/files/")))
        if ".." in relative.parts:
            self.send_error(HTTPStatus.NOT_FOUND)
            return
        candidate = ROOT.joinpath(*relative.parts).resolve()
        literature_root = (MEMORY / "literature").resolve()
        if literature_root not in candidate.parents or not candidate.is_file():
            self.send_error(HTTPStatus.NOT_FOUND)
            return
        raw = candidate.read_bytes()
        mime, _ = mimetypes.guess_type(candidate.name)
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", mime or "application/octet-stream")
        self.send_header("Content-Length", str(len(raw)))
        self.send_header("Cache-Control", "public, max-age=86400")
        self.end_headers()
        self.wfile.write(raw)

    def log_message(self, format_string: str, *args: Any) -> None:
        print(f"[{self.log_date_time_string()}] {format_string % args}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    refresh_bundle()
    server = ThreadingHTTPServer((args.host, args.port), ResearchHandler)
    print(f"Research Intelligence: http://{args.host}:{args.port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
