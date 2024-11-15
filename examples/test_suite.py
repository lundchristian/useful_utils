"""Example using the TestSuite class"""

import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(1, project_root)

from useful import TestSuite


class TestStuff(TestSuite):
    """A simple example test suite for testing your code"""

    def __init__(self) -> None:
        """Remember to call super().__init__() in the constructor"""
        self.local_var: int = 42
        super().__init__()

    def test_a(self) -> bool:
        """Example A: Should PASS"""
        return True

    def test_b(self) -> bool:
        """Example B: Should PASS"""
        return True

    def test_c(self) -> bool:
        """Example C: Should PASS"""
        return True


def main() -> None:
    """Runs the tests in random order"""
    suite = TestStuff()
    suite.run(random_order=True)


if __name__ == "__main__":
    main()
