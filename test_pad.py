import unittest

import main


class PadAndOverwriteTest(unittest.TestCase):
    def test_pad_filter(self):
        command = main.compile_workflow({
            "input": "input.mp4",
            "output": "output.mp4",
            "nodes": [
                {"type": "pad", "width": 1920, "height": 1080, "x": 100, "y": 20, "color": "black"}
            ],
        })
        value = command[command.index("-vf") + 1]
        self.assertEqual(value, "pad=1920:1080:100:20:black")

    def test_no_overwrite_flag(self):
        command = main.compile_workflow({
            "input": "input.mp4",
            "output": "output.mp4",
            "overwrite": False,
        })
        self.assertEqual(command[1], "-n")

    def test_default_overwrite_flag(self):
        command = main.compile_workflow({
            "input": "input.mp4",
            "output": "output.mp4",
        })
        self.assertEqual(command[1], "-y")

    def test_invalid_pad_color_is_rejected(self):
        with self.assertRaises(ValueError):
            main.compile_workflow({
                "input": "input.mp4",
                "output": "output.mp4",
                "nodes": [
                    {"type": "pad", "width": 1920, "height": 1080, "color": "black,scale=10:10"}
                ],
            })

    def test_overwrite_must_be_boolean(self):
        with self.assertRaises(ValueError):
            main.compile_workflow({
                "input": "input.mp4",
                "output": "output.mp4",
                "overwrite": "yes",
            })


if __name__ == "__main__":
    unittest.main()
