#!/usr/bin/python3
"""This module defines a classs model."""


class Base:
    """
    Represent the base model.
    Represents the "base" for all other classes in project 0x0C*.
    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """
    __nb_objects = 0
    def __init__(self, id = None):
        """
        Initialize a new base.

        Args:
            id(int): The id of the new base.
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
