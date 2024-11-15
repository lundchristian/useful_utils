# README

_Useful utilities, only standard library dependencies_

## Utility: Benchmark

Easily benchmark the bottlenecks in your code.

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

## TestSuite
