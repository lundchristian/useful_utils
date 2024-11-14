"""Example using the Benchmark class"""

import os
import sys
import array
import numpy as np
from functools import reduce

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from useful.Benchmark import Benchmark  # pylint: disable=C0413


class LoopWith:
    """Used for prepending names to the functions"""

    @staticmethod
    def for_each(a):
        """Benchmarking for each"""
        acc = 0
        for i in a:
            acc += i
        return acc

    @staticmethod
    def range_func(a):
        """Benchmarking range"""
        acc = 0
        for i in range(len(a)):  # pylint: disable=C0200
            acc += a[i]
        return acc

    @staticmethod
    def sum_func(a):
        """Benchmarking sum"""
        return sum(a)

    @staticmethod
    def numpy_sum_func(a):
        """Benchmarking numpy sum"""
        return np.sum(a)

    @staticmethod
    def reduce_func(a):
        """Benchmarking reduce"""
        return reduce(lambda x, y: x + y, a)


def main() -> None:
    """Entrypoint"""
    bench = (
        Benchmark()
        .add(LoopWith.for_each)
        .add(LoopWith.numpy_sum_func)
        .add(LoopWith.range_func)
        .add(LoopWith.sum_func)
        .add(LoopWith.reduce_func)
    )

    size = 10_000
    conditions = [
        ("list", list(range(size))),
        ("np.array", np.array(list(range(size)))),
        ("array", array.array("i", list(range(size)))),
    ]
    for condition in conditions:
        print(f"Benchmarking with {condition[0]}")
        bench(condition[1])


if __name__ == "__main__":
    main()
