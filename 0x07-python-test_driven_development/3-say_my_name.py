#!/usr/bin/python3
"""
    Write a function that prints My name is <first name> <last name>
    Prototype: def say_my_name(first_name, last_name=""):
"""


def say_my_name(first_name, last_name=""):
    """ print my first and last name """
    str_error = "first_name must be a string or last_name must be a string"
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError(str_error)
    print("My name is", first_name, last_name)
