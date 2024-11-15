"""Example using the Benchmark class"""

import os
import sys
from functools import reduce

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(1, project_root)

from useful import Benchmark


def loop_with_for_each(a):
    """Benchmarking for each"""
    acc = 0
    for i in a:
        acc += i
    return acc


def loop_with_range_func(a):
    """Benchmarking range"""
    acc = 0
    for i in range(len(a)):
        acc += a[i]
    return acc


def loop_with_sum_func(a):
    """Benchmarking sum"""
    return sum(a)


def loop_with_reduce_func(a):
    """Benchmarking reduce"""
    return reduce(lambda x, y: x + y, a)


def main() -> None:
    """Entrypoint"""
    bench = (
        Benchmark(unit="ms")
        .add(loop_with_for_each)
        .add(loop_with_range_func)
        .add(loop_with_sum_func)
        .add(loop_with_reduce_func)
    )

    bench.run(list(range(10_000)))


if __name__ == "__main__":
    main()
