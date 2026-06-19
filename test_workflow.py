import unittest

import main


class WorkflowValidationTest(unittest.TestCase):
    def test_input_and_output_must_differ(self):
        with self.assertRaises(ValueError):
            main.compile_workflow({"input": "same.mp4", "output": "same.mp4"})

    def test_trim_options_are_before_input(self):
        command = main.compile_workflow({
            "input": "input.mp4",
            "output": "output.mp4",
            "nodes": [{"type": "trim", "start": 5, "duration": 12}],
        })
        self.assertLess(command.index("-ss"), command.index("-i"))
        self.assertLess(command.index("-t"), command.index("-i"))

    def test_crop_and_scale_filters_keep_node_order(self):
        command = main.compile_workflow({
            "input": "input.mp4",
            "output": "output.mp4",
            "nodes": [
                {"type": "crop", "width": 1080, "height": 1080, "x": 100, "y": 0},
                {"type": "scale", "width": 720, "height": 720},
            ],
        })
        filters = command[command.index("-vf") + 1]
        self.assertEqual(filters, "crop=1080:1080:100:0,scale=720:720")

    def test_invalid_frame_rate_is_rejected(self):
        with self.assertRaises(ValueError):
            main.compile_workflow({
                "input": "input.mp4",
                "output": "output.mp4",
                "nodes": [{"type": "fps", "value": 0}],
            })


if __name__ == "__main__":
    unittest.main()
