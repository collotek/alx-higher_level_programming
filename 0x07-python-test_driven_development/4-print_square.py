#!/usr/bin/python3
"""
    Write a function that prints a square with
    the character #.
    Prototype: def print_square(size):
"""


def print_square(size):
    """ print a square """
    int_error = "size must be an integer"
    neg_error = "size must be >= 0"
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size, end="")
        print()
