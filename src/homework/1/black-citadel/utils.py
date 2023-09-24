"""Utility functions."""


def bold(string: str) -> str:
    """Wrap a string in ANSI escape codes to make it bold and blue when printed on the terminal.
    :param string: The string to format.
    :return: The formatted string.
    """
    return f"\033[1;36m{string}\033[0m"
