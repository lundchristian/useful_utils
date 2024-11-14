import time
import platform
from concurrent.futures import ProcessPoolExecutor, as_completed


class Benchmark:
    """Benchmarking class inspired by the Deno benchmarking tool"""

    def __init__(self, iterations: int = 100):
        self.function_list = []
        self.iterations = iterations

    def add(self, func):
        self.function_list.append(func)
        return self

    def _bench(self, func, *args, **kwargs):
        iteration_times = []
        for _ in range(self.iterations):
            start = time.perf_counter()
            _ = func(*args, **kwargs)
            stop = time.perf_counter()
            iteration_times.append(stop - start)

        avg = sum(iteration_times) / self.iterations
        return {
            "id": self.function_list.index(func),
            "name": func.__name__,
            "sec": avg,
            "ms": avg * 1_000,
            "max_ms": max(iteration_times) * 1_000,
            "min_ms": min(iteration_times) * 1_000,
            "us": avg * 1_000_000,
            "ns": avg * 1_000_000_000,
        }

    def __call__(self, *args, **kwargs):
        results = []

        with ProcessPoolExecutor() as executor:
            futures = []
            for func in self.function_list:
                futures.append(executor.submit(self._bench, func, *args, **kwargs))
            for future in as_completed(futures):
                results.append(future.result())

        self.print(results)

    def print(self, results):
        print()
        print(f"System:     {platform.system()} {platform.machine()}")
        print(f"Iterations: {self.iterations}")
        print()

        results = sorted(results, key=lambda x: x["sec"])
        lfn = max(len(func.__name__) for func in self.function_list)

        for result in results:
            string = f"Test: {result['name']:<{lfn}} | "
            string += f"Avg: {result['ms']:<7.3f} ms | "
            string += f"Max: {result['max_ms']:<7.3f} ms | "
            string += f"Min: {result['min_ms']:<7.3f} ms"
            print(string)

        print()
        for i, result in enumerate(results):
            if i == 0:
                continue
            slower = result["ms"] / results[0]["ms"]
            string = f"\tx{round(slower, 2):<7} slower: {result['name']:<{lfn}}"
            print(string)
        print()
