import random


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
        self.test_functions: list[callable] = [
            getattr(self, func)
            for func in dir(self)
            if callable(getattr(self, func)) and func.startswith("test_")
        ]

    def _pass(self) -> str:
        """Note: Note: Intended as private method!

        Returns '[+] PASS' formatted in green
        """
        return "\033[92m[+] PASS\033[0m"

    def _fail(self) -> str:
        """Note: Note: Intended as private method!

        Returns '[-] FAIL' formatted in red
        """
        return "\033[91m[-] FAIL\033[0m"

    def _skip(self) -> str:
        """Note: Note: Intended as private method!

        Returns '[~] SKIP' formatted in yellow
        """
        return "\033[93m[~] SKIP\033[0m"

    def _run_tests(self, tests: list[callable]) -> bool:
        """Note: Note: Intended as private method!

        Runs all the tests in the list and prints the results.

        Args:
            tests (list[callable]): A list of test functions to run.

        Returns:
            bool: True if all tests pass, False otherwise.
        """

        passed: int = 0
        num_tests: int = len(tests)

        for test in tests:
            result = test()
            assert (
                isinstance(result, bool) or result == 0 or result == 1
            ), "Test functions must return a boolean value or 0/1"
            passed += int(result)
            print(f"{self._pass() if result else self._fail()}\t{test.__doc__}")

        percent: float = (passed / num_tests) * 100
        print(f"\n{passed} OF {num_tests} ({percent:.2f}%) TESTS PASSED\n")
        return passed == num_tests

    def run(self, random_order: bool = False) -> None:
        """Runs all the tests in the test suite.

        Args:
            random_order (bool):
                If True, tests will be run in a random order. Defaults to False.
        """

        assert self.test_functions, "No tests found in test suite"

        print("\n[~] SEQUENTIAL TEST RUN\n")
        sequential_passed: bool = self._run_tests(self.test_functions)
        if random_order and sequential_passed:
            print("[~] RUNNING TEST RUN\n")
            random.shuffle(self.test_functions)
            self._run_tests(self.test_functions)
        elif random_order and not sequential_passed:
            print("[~] TESTS MUST PASS IN SEQUENTIAL ORDER FIRST\n")
