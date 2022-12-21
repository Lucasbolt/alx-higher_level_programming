#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """
        initialize a new square.

        Args:
            size (int): the size of the new square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if size is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be > 0')
        self.__size = size

    def area(self):
        """computes aras of Square"""
        return self.__size * self.__size
