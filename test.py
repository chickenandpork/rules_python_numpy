# This is exactly https://github.com/bazelbuild/rules_python/blob/main/examples/pip_parse/test.py @018e355

import unittest
import main


class ExampleTest(unittest.TestCase):
    """This is a known-good unittest to confirm that Bazel py_test() is functional"""

    def test_main(self):
        self.assertEqual("2.25.1", main.version())


if __name__ == "__main__":
    unittest.main()
