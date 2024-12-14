import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(1, project_root)

from useful import TestSuite


class TestTestSuite(TestSuite):
    """Testing the TestSuite using the TestSuite"""

    def test_no_functions(self) -> bool:
        """Test that no functions will result in a failure"""
        uut = TestSuite()
        try:
            uut.run()
            return False
        except AssertionError:
            return True


def main() -> None:
    suite = TestTestSuite()
    suite.run()


if __name__ == "__main__":
    main()
