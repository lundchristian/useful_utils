import time
from concurrent.futures import ProcessPoolExecutor, as_completed


class Benchmark:
    """Benchmarking class inspired by the Deno benchmarking tool"""

    def __init__(self, iterations: int = 100, unit: str = "ms"):
        assert iterations > 0, "Iterations must be greater than 0"
        assert unit in [
            "ns",
            "us",
            "ms",
            "sec",
        ], "Unit must be 'ns', 'us', 'ms', or 'sec'"
        self.function_list = []
        self.iterations = iterations
        self.unit = unit

    def add(self, func):
        self.function_list.append(func)
        return self

    def _grn(self, msg: str) -> str:
        """Returns '[+] {msg}' formatted in green"""
        return f"\033[92m[+] {msg}\033[0m"

    def _red(self, msg: str) -> str:
        """Returns '[-] {msg}' formatted in red"""
        return f"\033[91m[-] {msg}\033[0m"

    def _bench(self, func, *args, **kwargs):
        iteration_times = []
        for _ in range(self.iterations):
            start = time.perf_counter()
            _ = func(*args, **kwargs)
            stop = time.perf_counter()
            iteration_times.append(stop - start)

        avg = sum(iteration_times) / self.iterations
        max_sec = max(iteration_times)
        min_sec = min(iteration_times)
        return {
            "id": self.function_list.index(func),
            "name": func.__name__,
            "sec": avg,
            "max_sec": max_sec,
            "min_sec": min_sec,
            "ms": avg * 1_000,
            "max_ms": max_sec * 1_000,
            "min_ms": min_sec * 1_000,
            "us": avg * 1_000_000,
            "max_us": max_sec * 1_000_000,
            "min_us": min_sec * 1_000_000,
            "ns": avg * 1_000_000_000,
            "max_ns": max_sec * 1_000_000_000,
            "min_ns": min_sec * 1_000_000_000,
        }

    def run(self, *args, **kwargs):
        results = []

        with ProcessPoolExecutor() as executor:
            futures = []
            for function in self.function_list:
                called = executor.submit(self._bench, function, *args, **kwargs)
                futures.append(called)
            for future in as_completed(futures):
                results.append(future.result())

        self.print(results)

    def print(self, results):
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
