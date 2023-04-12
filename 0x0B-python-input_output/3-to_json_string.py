#!/usr/bin/python3
"""Defines function json representation of a string."""
import json


def to_json_string(my_obj):
    """Return JSON representation of an object."""
    return json.dumps(my_obj)
