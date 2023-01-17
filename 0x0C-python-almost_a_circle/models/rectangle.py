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
        return self.__y

    @y.setter
    def y(self, val):
        if type(val) != int:
            raise TypeError('y must be an integer')
        if val < 0:
            raise ValueError('y must be >= 0')
        self.__y = val

    def area(self):
        """Returns the area of a rectangle instance."""
        return self.width * self.height

    def __str__(self):
        """Overloading the __str__ method."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
    def update(self, *args, **kwargs):
        """Update the Rectangle.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
