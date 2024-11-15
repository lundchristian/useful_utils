# README

_Useful utilities, only standard library dependencies_

## Get Started

Raw installation.

```bash
pip install useful-utils
```

Virtual environment installation.

```bash
python -m venv .venv
source .venv/bin/activate
pip install useful-utils
```

## Utilities

### Benchmark

Easily benchmark bottlenecks in your code.

1. Identify the hotspot
2. Isolate the hotspot code
3. Implement different alternative approaches
4. Benchmark the alternatives

```python
from useful import Benchmark

def alternative_a():
    pass # perform some operation
def alternative_b():
    pass # perform some operation

def alternative_c(parameter):
    pass # perform some operation using the argument
def alternative_d(parameter):
    pass # perform some operation using the argument

def example_1():
    bench = Benchmark(
            iterations = 100, # default | alternatives: argument > 0
            unit = "ms" # default | alternatives: "sec", "ms", "us", "ns"
        ).add(alternative_a).add(alternative_b)
    bench.run()

def example_2():
    bench = Benchmark().add(alternative_c).add(alternative_d)
    bench.run(42) # pass in argument of choice

if __name__ == "__main__":
    example_1()
    example_2()
```

```bash
Iterations: 100

Test: alternative_a    | Avg: 0.080 ms | Max: 0.105 ms | Min: 0.078 ms
Test: alternative_b    | Avg: 0.430 ms | Max: 0.818 ms | Min: 0.359 ms

[+] x1.0     alternative_a
[-] x5.35    alternative_b
```

### TestSuite

Easily test your code without all of the usual overhead and complex
configurations.

```python
from useful import TestSuite

class TestStuff(TestSuite):
    def test_a(self) -> bool:
        return True

    def test_b(self) -> bool:
        return False

    def test_c(self) -> bool:
        return True

if __name__ == "__main__":
    suite = TestStuff()
    suite.run(random_order=False) # default | alternatives: True, False
```

```bash
[~] SEQUENTIAL TEST RUN

[+] PASS        Example: Should PASS
[-] FAIL        Example: Should FAIL
[+] PASS        Example: Should PASS

2 OF 3 (66.67%) TESTS PASSED
```

## Structure

The `useful` directory is equivalent to the common `src` directory, here you
will find the implementations.

The `examples` directory contains some simple examples showcasing intended usage
of the utilities.

The `test` directory contains all tests.

    .
    ├── examples
    │   ├── benchmark.py
    │   └── test_suite.py
    ├── test
    │   ├── benchmark.py
    │   └── test_suite.py
    └── useful
        ├── __init__.py
        ├── benchmark.py
        └── test_suite.py
