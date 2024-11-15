import time
from concurrent.futures import ProcessPoolExecutor, as_completed


class Benchmark:
    """
    Benchmark class to measure the performance of functions.

    Usage:
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
    """

    def __init__(self, iterations: int = 100, unit: str = "ms") -> None:
        """Initialize the Benchmark class.

        Args:
            iterations (int, optional):
                Number of iterations to run the benchmark. The average time
                will be calculated from these iterations. The more iterations,
                the more accurate the average time will be. Defaults to 100.
            unit (str, optional):
                Unit of time to display the results in. Can be "ns"
                (nanoseconds), "us" (microseconds), "ms" (milliseconds),
                or "sec" (seconds). Defaults to "ms".
        """
        assert iterations > 0, "Iterations must be greater than 0"
        assert unit in [
            "ns",
            "us",
            "ms",
            "sec",
        ], "Unit must be 'ns', 'us', 'ms', or 'sec'"

        self.function_list = []
        self.unit = unit
        self.iterations = iterations

    def _grn(self, msg: str) -> str:
        """Note: Intended as private method!

        Returns '[+] {msg}' formatted in green
        """
        return f"\033[92m[+] {msg}\033[0m"

    def _red(self, msg: str) -> str:
        """Note: Intended as private method!

        Returns '[-] {msg}' formatted in red
        """
        return f"\033[91m[-] {msg}\033[0m"

    def _bench(self, func, *args, **kwargs):
        """Note: Intended as private method!

        Executes the function and returns the average time taken to execute.
        """
        iteration_times = []

        for _ in range(self.iterations):
            start = time.perf_counter()
            _ = func(*args, **kwargs)
            stop = time.perf_counter()
            iteration_times.append(stop - start)

        avg_sec = sum(iteration_times) / self.iterations
        max_sec = max(iteration_times)
        min_sec = min(iteration_times)

        return {
            "id": self.function_list.index(func),
            "name": func.__name__,
            "sec": avg_sec,
            "max_sec": max_sec,
            "min_sec": min_sec,
            "ms": avg_sec * 1_000,
            "max_ms": max_sec * 1_000,
            "min_ms": min_sec * 1_000,
            "us": avg_sec * 1_000_000,
            "max_us": max_sec * 1_000_000,
            "min_us": min_sec * 1_000_000,
            "ns": avg_sec * 1_000_000_000,
            "max_ns": max_sec * 1_000_000_000,
            "min_ns": min_sec * 1_000_000_000,
        }

    def _print(self, results):
        """Note: Intended as private method!

        Prints the results of the benchmark formatted nicely.
        """
        print()
        print(f"Iterations: {self.iterations}")
        print()

        results = sorted(results, key=lambda x: x["sec"])
        lfn = max(len(func.__name__) for func in self.function_list)
        lbr = max(len(f"{result[self.unit]:.3f}") for result in results)
        lmr = max(len(f"{result[f'max_{self.unit}']:.3f}") for result in results)

        for result in results:
            string = f"Test: {result['name']:<{lfn}} | "
            string += f"Avg: {result[self.unit]:<{lbr}.3f} {self.unit} | "
            string += f"Max: {result[f'max_{self.unit}']:<{lmr}.3f} {self.unit} | "
            string += f"Min: {result[f'min_{self.unit}']:<{lbr}.3f} {self.unit}"
            print(string)

        print()
        for i, result in enumerate(results):
            slower = result[self.unit] / results[0][self.unit]
            string = f"x{round(slower, 2):<7} {result['name']:<{lfn}}"
            string = self._red(string) if i != 0 else self._grn(string)
            print(string)
        print()

    def add(self, function):
        """Add a function to the benchmarking execution list.

        Args:
            function (callable): Function to add to the benchmarking list.

        Returns:
            self: In order to chain multiple function calls.
        """
        self.function_list.append(function)
        return self

    def run(self, *args, **kwargs):
        """Benchmark all of the functions added to the execution list."""

        assert self.function_list, "No functions to benchmark"

        results = []

        with ProcessPoolExecutor() as executor:
            futures = []
            for function in self.function_list:
                called = executor.submit(self._bench, function, *args, **kwargs)
                futures.append(called)
            for future in as_completed(futures):
                results.append(future.result())

        self._print(results)
