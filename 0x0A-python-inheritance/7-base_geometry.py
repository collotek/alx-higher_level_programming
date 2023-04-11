#!/usr/bin/python3
"""Defines base class BaseGeometry."""


class BaseGeometry:
    """Represents a base geometry."""

    def area(self):
        """Not implemented yet."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate parameter as integer.
        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
