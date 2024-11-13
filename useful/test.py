"""
Author: Christian Lund
Date: 2024-10-02
Testing the TestSuite
"""

from TestSuite import TestSuite  # pylint: disable=E0401


def main() -> None:
    """Testing the TestSuite"""
    uut_no_tests = TestSuite()
    # pylint: disable=W0212
    assert "\033[92m[+] PASS\033[0m" == uut_no_tests._pass(), "TestSuite._pass() failed"
    assert "\033[91m[-] FAIL\033[0m" == uut_no_tests._fail(), "TestSuite._fail() failed"
    assert "\033[93m[~] SKIP\033[0m" == uut_no_tests._skip(), "TestSuite._skip() failed"
    assert not uut_no_tests._any_tests(), "TestSuite._any_tests() failed"
    # pylint: enable=W0212
    print("All tests passed!")


if __name__ == "__main__":
    main()
