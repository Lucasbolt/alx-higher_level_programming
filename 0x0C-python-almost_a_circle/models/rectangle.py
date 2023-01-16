#!/usr/bin/python3
"""This module defines a class - Rectangle."""
from models.base import Base


class Rectangle(Base):
    """ Defines the Rectangle class.
    Inherit attributes from the Base class.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get/set width."""
        return self.__width

    @width.setter
    def width(self, val):
        if type(val) != int:
            raise TypeError('width must be an integer')
        if val <= 0:
            raise ValueError('width must be > 0')
        self.__width = val

    @property
    def height(self):
        """ get/set height"""
        return self.__height

    @height.setter
    def height(self, val):
        if type(val) != int:
            raise TypeError('height must be an integer')
        if val <= 0:
            raise ValueError('height must be > 0')
        self.__height = val

    @property
    def x(self):
        """get/set x."""
        return self.__x

    @x.setter
    def x(self, val):
        if type(val) != int:
            raise TypeError('x must be an integer')
        if val < 0:
            raise ValueError('x must be >= 0')
        self.__x = val

    @property
    def y(self):
        """get/set y cordinate of a rectangle."""

    @y.setter
    def y(self, val):
        if type(val) != int:
            raise TypeError('y must be an integer')
        if val < 0:
            raise ValueError('y must be >= 0')
        self.__y = val
