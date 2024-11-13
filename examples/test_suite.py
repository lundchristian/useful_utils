"""Example of how to use the TestSuite class to run tests"""

from useful import TestSuite


class TestStuff(TestSuite):
    """A simple example test suite for testing your code"""

    def __init__(self) -> None:
        """Remember to call super().__init__() in the constructor"""
        self.local_var: int = 42
        super().__init__()

    def test_a(self) -> bool:
        """Testing that a is true"""
        return True

    def test_b(self) -> bool:
        """Testing that b is true"""
        return True

    def test_c(self) -> bool:
        """Testing that c is true"""
        return True


def main() -> None:
    """Runs the tests in random order"""
    suite = TestStuff()
    suite.run(random_order=True)


if __name__ == "__main__":
    main()
