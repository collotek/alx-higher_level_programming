#!/usr/bin/python3
"""module comment inserted here"""


class Rectangle:
    """ definition of class rectangle """

    def __init__(self, width=0, height=0):
        """ initializing width and height """
        self.height = height
        self.width = width

    @property
    def height(self):
        """ gets height """
        return self.__height

    @property
    def width(self):
        """ gets the width """
        return self.__width

    @height.setter
    def height(self, value):
        """ this setter sets the height with a new value """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """ sets the width with a new value """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """ returns area of the rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ returns the perimeter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)
