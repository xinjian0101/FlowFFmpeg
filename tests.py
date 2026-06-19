import unittest
import main


class CompilerTest(unittest.TestCase):
    def test_scale_node(self):
        workflow = {"input": "input.mov", "output": "output.mov", "nodes": [{"type": "scale", "height": 720}]}
        command = main.compile_workflow(workflow)
        self.assertTrue(any("scale=" in part for part in command))


if __name__ == "__main__":
    unittest.main()
