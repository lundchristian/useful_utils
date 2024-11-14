# pylint: disable=C0103
"""
Author: Christian Lund
Date: 2024-10-02
A simple test suite for testing your code.
"""

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

        This function should be called in the constructor of the
        subclass. It will automatically find all test functions
        in the subclass and store them in a list.
        """
        self.test_functions: list[callable] = [
            getattr(self, func)
            for func in dir(self)
            if callable(getattr(self, func)) and func.startswith("test_")
        ]

    def _pass(self) -> str:
        """Returns '[+] PASS' formatted in green"""
        return "\033[92m[+] PASS\033[0m"

    def _fail(self) -> str:
        """Returns '[-] FAIL' formatted in red"""
        return "\033[91m[-] FAIL\033[0m"

    def _skip(self) -> str:
        """Returns '[~] SKIP' formatted in yellow"""
        return "\033[93m[~] SKIP\033[0m"

    def _run_tests(self, tests: list[callable]) -> bool:
        """Runs all the tests in the list and prints the results.

        Args:
            tests (list[callable]): A list of test functions to run.

        Returns:
            bool: True if all tests pass, False otherwise.
        """
        passed: int = 0
        num_tests: int = len(tests)
        for test in tests:
            result = test()
            passed += int(result)
            print(f"{self._pass() if result else self._fail()}\t{test.__doc__}")
        percent: float = (passed / num_tests) * 100
        print(f"\n{passed} OF {num_tests} ({(percent):.2f}%) TESTS PASSED\n")
        return passed == num_tests

    def _any_tests(self) -> bool:
        """Returns True if there are any tests in the test suite.

        Returns:
            bool: True if there are any tests, False otherwise.
        """
        return len(self.test_functions) > 0

    def print_tests(self) -> None:
        """Prints out all the test functions in the test suite."""
        if not self._any_tests():
            print("[~] NOTHING TO TEST\n")
            return
        for test in self.test_functions:
            print(test.__doc__)

    def run(self, random_order: bool = False) -> None:
        """Runs all the tests in the test suite.

        Args:
            random_order (bool): If True, tests will be run in a random order.
        """
        if not self._any_tests():
            print("[~] NOTHING TO TEST\n")
            return
        print("[~] SEQUENTIAL TEST RUN\n")
        sequential_passed: bool = self._run_tests(self.test_functions)
        if random_order and sequential_passed:
            print("[~] RUNNING TEST RUN\n")
            random.shuffle(self.test_functions)
            self._run_tests(self.test_functions)
        elif random_order and not sequential_passed:
            print("[~] TESTS MUST PASS IN SEQUENTIAL ORDER FIRST\n")
