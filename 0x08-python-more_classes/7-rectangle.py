#!/usr/bin/python3
"""module comment here"""


class Rectangle:
    """ defining an empty rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initializing width and height """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """ height getter"""
        return self.__height

    @property
    def width(self):
        """ width getter"""
        return self.__width

    @height.setter
    def height(self, value):
        """ sets height with new value """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """ set width with new value """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """ returns of rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ returns rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """ return rectangle string with # """
        string = ""
        if self.__height == 0 or self.__width == 0:
            return string
        for i in range(self.__height):
            string += (str(self.print_symbol) * self.__width)
            if i < self.__height - 1:
                string += '\n'
        return string

    def __repr__(self):
        """ return rectangle representation"""
        return "Rectangle(" + str(self.__width) + ","\
                            + str(self.__height) + ")"

    def __del__(self):
        """ deleting the instance """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
