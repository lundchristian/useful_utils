"""Testing the Benchmark class"""

import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(1, project_root)

from useful import Benchmark
from useful import TestSuite


class TestBenchmark(TestSuite):
    """Test suite for the Benchmark class"""

    def test_no_functions(self) -> None:
        uut = Benchmark()
        try:
            uut.run()
            return False
        except AssertionError:
            return True


def main() -> None:
    """Entrypoint"""
    suite = TestBenchmark()
    suite.run()


if __name__ == "__main__":
    main()
