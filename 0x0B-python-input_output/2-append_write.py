#!/usr/bin/python3
"""Defines function that appends a string at end of text file."""


def append_write(filename="", text=""):
    """Appends string at end of text file.
    Args:
        filename (str): name of file to append to.
        text (str): string to append to the file.
    Returns:
        number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
