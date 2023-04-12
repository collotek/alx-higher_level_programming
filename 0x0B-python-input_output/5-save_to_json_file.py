#!/usr/bin/python3
"""Defines function that writes an Object to text file"""
import json


def save_to_json_file(my_obj, filename):
    """object to a text file that uses JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
