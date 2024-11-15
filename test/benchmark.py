"""Testing the Benchmark class"""

import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(1, project_root)

from useful.benchmark import Benchmark  # pylint: disable=C0413


def main() -> None:
    """Entrypoint"""
    uut = Benchmark()


if __name__ == "__main__":
    main()
