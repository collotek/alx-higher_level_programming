#!/usr/bin/python3
"""Insert module comment here"""


class Rectangle:
    """ defines an empty class rectangle """

    def __init__(self, width=0, height=0):
        """ initializing width and height """
        self.height = height
        self.width = width

    @property
    def height(self):
        """ retrieve height """
        return self.__height

    @property
    def width(self):
        """ retrieve width """
        return self.__width

    @height.setter
    def height(self, value):
        """ sets the height with new value """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """ sets the width to a new value """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """ returns area of the rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ returns perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """ representation of rectangle with # """
        string = ""
        if self.__height == 0 or self.__width == 0:
            return string
        for i in range(self.__height):
            string += ("#" * self.__width)
            if i < self.__height - 1:
                string += '\n'
        return string
