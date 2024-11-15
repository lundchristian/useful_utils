"""
Note: This module contains common private functions that are used across
multiple modules.
"""


def okay(msg: str) -> str:
    """Returns '[+] {msg}' formatted in green"""
    return f"\033[92m[+] {msg}\033[0m"


def note(msg: str) -> str:
    """Returns '[~] {msg}' formatted in yellow"""
    return f"\033[93m[~] {msg}\033[0m"


def fail(msg: str) -> str:
    """Returns '[-] {msg}' formatted in red"""
    return f"\033[91m[-] {msg}\033[0m"
