# 合法全文下载与论文解析工具选型

本项目只下载出版社、开放仓库或开放获取索引明确给出的合法 PDF，不接入 Sci-Hub 或绕过付费墙的工具。

## 下载与解析链路

1. OpenAlex / Semantic Scholar 提供题录、OA 状态和候选 PDF。
2. DOI 出版社页面中的 `citation_pdf_url` 作为第二解析入口。
3. 使用 `UNPAYWALL_EMAIL`（默认采用仓库公开的 GitHub noreply 地址）查询作者稿、PMC/DOAJ 仓储版本或出版社 OA 版本。
4. 只有响应是实际 PDF 且小于 40 MB 时才归档。
5. PyMuPDF / PDFPlumber 负责本地文本、页码、图注和图像提取。

## 已核对的 GitHub 工具

| 工具 | 用途 | 集成判断 |
|---|---|---|
| [unpywall/unpywall](https://github.com/unpywall/unpywall) | Python 调用 Unpaywall | 可选；当前先直接调用 REST API，减少依赖 |
| [grobidOrg/grobid](https://github.com/grobidOrg/grobid) | 学术 PDF 转 TEI XML，识别章节、参考文献和图注 | 推荐作为后续高精度服务，需要 Java 容器 |
| [allenai/pdffigures2](https://github.com/allenai/pdffigures2) | 提取图、表、图注和章节标题 | 适合逐图裁切，需要 Scala/Java 运行环境 |
| [docling-project/docling](https://github.com/docling-project/docling) | PDF 转结构化文档/Markdown/JSON | 推荐的 Python 增强后端，依赖和模型较大 |
| [datalab-to/marker](https://github.com/datalab-to/marker) | PDF 转 Markdown/JSON | 精度高但依赖较重，GPL-3.0，暂不作为默认依赖 |
| [jannisborn/paperscraper](https://github.com/jannisborn/paperscraper) | PubMed/arXiv 等题录检索 | 可补充检索，不负责绕过出版社访问控制 |

当前默认实现选择“无外部服务也能运行”的 PyMuPDF/PDFPlumber 路径；GROBID、Docling 和 pdffigures2 作为可替换增强后端。
