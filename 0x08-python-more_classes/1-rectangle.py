#!/usr/bin/python3
"""module comment goes here"""


class Rectangle:
    """ defines an empty class rectangle """

    def __init__(self, width=0, height=0):
        """ height and width are initialized"""
        self.height = height
        self.width = width

    @property
    def height(self):
        """ gets the height """
        return self.__height

    @property
    def width(self):
        """ gets the width """
        return self.__width

    @height.setter
    def height(self, value):
        """ sets the height value """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """ sets the width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
