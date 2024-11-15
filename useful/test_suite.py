import random

from useful.common import okay, fail


class TestSuite:
    """
    TestSuite enables simple testing of your code.

    Inherit from the class, and name all your test functions like so:

    def test_*(self) -> bool

    Make sure to return true or false depending on the output.

    If you define a constructor, make sure to call super().__init__().
    """

    def __init__(self) -> None:
        """Initializes the test suite with all test functions.

        If you define a custom constructor, make sure to call
        super().__init__() as it will automatically find all test functions.
        """
        self._test_functions: list[callable] = []
        for function in dir(self):
            if callable(getattr(self, function)) and function.startswith("test_"):
                self._test_functions.append(getattr(self, function))

    def _run_tests(self, tests: list[callable]) -> bool:
        """Note: Note: Intended as private method!

        Runs all the tests in the list and prints the results.
        """

        passed: int = 0
        total: int = len(tests)
        results: list[tuple[str, bool]] = []

        for test in tests:
            result = test()
            assert int(result) in [0, 1], "Test functions must return boolean values"
            passed += int(result)
            results.append((test.__doc__, result))

        return {
            "outcomes": results,
            "passed": passed,
            "total": total,
            "percent": (passed / total) * 100,
        }

    def _process_results(self, results: dict[str, any]) -> bool:
        """Note: Note: Intended as private method!

        Processes the results of the test run and prints them to the console.
        """
        outcomes: list[tuple[str, bool]] = results["outcomes"]
        passed: int = results["passed"]
        num_tests: int = results["total"]
        percent: float = results["percent"]
        self._print_results(outcomes, passed, num_tests, percent)
        return passed == num_tests

    def _print_results(
        self,
        outcomes: list[tuple[str, bool]],
        passed: int,
        num_tests: int,
        percent: float,
    ) -> None:
        """Note: Note: Intended as private method!

        Prints the results of the test run to the console.
        """
        for name, outcome in outcomes:
            print(f"{okay('PASS') if outcome else fail('FAIL')}\t{name}")
        print(f"\n{passed} OF {num_tests} ({percent:.2f}%) TESTS PASSED\n")

    def run(self, random_order: bool = False) -> bool:
        """Runs all the tests in the test suite.

        Args:
            random_order (bool):
                If True, tests will be run in a random order. Defaults to False.

        Returns:
            bool: True if all tests pass, False otherwise.
        """

        assert self._test_functions, "No tests found in test suite"

        print("\n[~] SEQUENTIAL TEST RUN\n")
        sequential_results: dict[str, any] = self._run_tests(self._test_functions)
        sequential_passed: bool = self._process_results(sequential_results)
        result: bool = sequential_passed

        if random_order:
            if not sequential_passed:
                print("[~] TESTS MUST PASS IN SEQUENTIAL ORDER FIRST\n")
            else:
                print("[~] RANDOM TEST RUN\n")
                random.shuffle(self._test_functions)
                random_results: dict[str, any] = self._run_tests(self._test_functions)
                random_passed: bool = self._process_results(random_results)
                result = random_passed

        return result
