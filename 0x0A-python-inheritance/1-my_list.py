#!/usr/bin/python3
"""Defines list class MyList which is inherited."""


class MyList(list):
    """Implements sorted printing for the list class."""

    def print_sorted(self):
        """Print list in sorted (ascending sort)"""
        print(sorted(self))
