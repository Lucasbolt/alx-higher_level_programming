#!/usr/bin/python3
# 1-square.py
"""Define a class Square and a private instance attribute (size)"""


class Square:
    """Represent a square"""

    def _init_(self, size):
        """initialize a new square.

        Args:
            size(int): The size of the square.
        """
        self.__size = size
