import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(1, project_root)

from useful import TestSuite


class MetaTestSuite(TestSuite):
    """Testing the TestSuite using the TestSuite"""

    def test_pass_color(self) -> bool:
        """Test the color of the pass message"""
        return "\033[92m[+] PASS\033[0m" == self._grn()

    def test_fail_color(self) -> bool:
        """Test the color of the fail message"""
        return "\033[91m[-] FAIL\033[0m" == self._red()

    def test_skip_color(self) -> bool:
        """Test the color of the skip message"""
        return "\033[93m[~] SKIP\033[0m" == self._skip()


def main() -> None:
    """Entrypoint"""
    uut = MetaTestSuite()
    uut.run()


if __name__ == "__main__":
    main()
