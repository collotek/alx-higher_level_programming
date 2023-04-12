#!/usr/bin/python3
"""Defines a function to write string to text file."""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF8).
    Args:
        filename (str): file name to write.
        text (str): text to be written into the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
