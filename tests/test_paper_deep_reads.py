from __future__ import annotations

import unittest

from scripts.build_paper_deep_reads import (
    extract_method_blocks,
    extract_preparation_steps,
    preparation_category,
    reading_note_zh,
    split_panel_caption,
)


class PaperDeepReadTests(unittest.TestCase):
    def test_split_panel_caption(self) -> None:
        panels = split_panel_caption("Fig. 2. (a) Device structure. (b) Calibration results. (c) Robot grasping.")
        self.assertEqual([panel["label"] for panel in panels], ["a", "b", "c"])
        self.assertIn("Device structure", panels[0]["original"])

    def test_split_uppercase_panel_caption(self) -> None:
        panels = split_panel_caption("Figure 1. A. Device structure. B. Calibration results. C. Robot grasping.")
        self.assertEqual([panel["label"] for panel in panels], ["a", "b", "c"])

    def test_split_nature_style_panel_caption_and_range(self) -> None:
        panels = split_panel_caption(
            "Fig. 4 Sensor response. a Structure. b–d Optical images. e Brightness. f–h Calibration."
        )
        self.assertEqual([panel["label"] for panel in panels], ["a", "b-d", "e", "f-h"])

    def test_split_nature_style_grouped_panels(self) -> None:
        panels = split_panel_caption("Fig. 3 Analysis. a, b Models. c Simulation results.")
        self.assertEqual([panel["label"] for panel in panels], ["a,b", "c"])

    def test_preparation_category(self) -> None:
        self.assertEqual(preparation_category("The solution was stirred for 2 h."), "材料混合与分散")
        self.assertEqual(preparation_category("The film was cured at 80 C."), "固化与热处理")

    def test_reading_note(self) -> None:
        self.assertIn("标定", reading_note_zh("Force calibration and linearity error"))

    def test_embedded_materials_heading_starts_method_extraction(self) -> None:
        blocks = [
            {"page": 1, "bbox": [0, 0, 1, 1], "text": "Signals are linearly mixed for reconstruction."},
            {"page": 2, "bbox": [0, 0, 1, 1], "text": "Conclusion text. MATERIALS AND METHODS"},
            {"page": 2, "bbox": [0, 0, 1, 1], "text": "The array was constructed using flexible circuit boards."},
            {"page": 2, "bbox": [0, 0, 1, 1], "text": "The electrodes were uniformly coated with Velostat."},
        ]
        methods = extract_method_blocks(blocks)
        self.assertEqual(len(methods), 2)
        self.assertIn("constructed", methods[0]["text"])

    def test_preparation_steps_exclude_conceptual_mixing(self) -> None:
        blocks = [
            {"page": 2, "bbox": [0, 0, 1, 1], "text": "The array was constructed using flexible circuit boards."},
            {"page": 2, "bbox": [0, 0, 1, 1], "text": "The electrodes were uniformly coated with Velostat."},
            {"page": 2, "bbox": [0, 0, 1, 1], "text": "The setup uses a 3-D printed probe and a UV laser."},
        ]
        steps = extract_preparation_steps(blocks)
        self.assertEqual([step["category_zh"] for step in steps], ["组装与封装", "成膜与沉积"])

    def test_two_column_method_flow_stops_before_back_matter(self) -> None:
        blocks = [
            {"page": 1, "bbox": [300, 80, 540, 150], "text": "4 h. The film was laser patterned."},
            {"page": 1, "bbox": [55, 80, 290, 400], "text": "Discussion and outlook text."},
            {"page": 1, "bbox": [300, 500, 540, 560], "text": "Acknowledgements Funding support."},
            {"page": 1, "bbox": [55, 420, 290, 720], "text": "Methods Device fabrication. The polymer was cured at 70 C for"},
        ]
        methods = extract_method_blocks(blocks)
        steps = extract_preparation_steps(methods)
        self.assertEqual(len(methods), 2)
        self.assertEqual(len(steps), 2)
        self.assertIn("70 C for 4 h", steps[0]["original"])


if __name__ == "__main__":
    unittest.main()
