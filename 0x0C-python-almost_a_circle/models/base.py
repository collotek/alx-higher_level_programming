#!/usr/bin/python3

"""Defines class: Base"""


Class Base:
    """ Base class
    This class will be the “base” of all other classes in this project.

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):

        """Initializing a new Base.
        Args:
            id (int): New Base Identity.
        """

        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects++
            self.id = Base.__nb_objects
