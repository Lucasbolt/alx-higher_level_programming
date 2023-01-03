#!/usr/bin/python3
"""
This module defines a class - Rectangle.
"""

class Rectangle:
    """
    creates a rectangle.

    Args:
        width(int): width of the rectangle (must be greater than 0).
        height(int): height of the rectangle (must be greater than 0).

    Raises:
        ValueError: this is raised if either `width` or `height` is < 0.
        TypeError: this is raised if either of `width` or `height` is not int.
    """

    def __init__(self, width=0, height=0):
        """
        instantiate values.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        to retrieve width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        to set width of rectangle.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        to retrieve height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        to set the height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value


