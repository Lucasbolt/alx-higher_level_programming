#!/usr/bin/python3
"""
This module defines a class - Rectangle.
"""


class Rectangle:
    """
    create a rectangle object.

    Args:
        width(int): width of the rectangle.
        height(int): height of the rectangle.

    Raise:
        TypeError: if either `width` or `height` is not int.
        ValueError: if either `width` or `height` is < 0.
    """


    def __init__(self, width=0, height=0):
        """
        instantiates a new rectangle object.
        """
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """
        Get / sets the value of width of rectangle object.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        fetch / set the value of `height` of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        computes the area of the rectangle object.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        computes the perimeter of the rectangle object.
        """
        if (self.__width or self.__height) == 0:
            return 0
        return 2 * (self.__height + self.__width)
