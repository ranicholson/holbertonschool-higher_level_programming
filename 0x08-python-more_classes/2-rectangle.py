#!/usr/bin/python3

"""Defining the Rectangle class"""


class Rectangle:

    """Attributes that make up the Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initializing of a new Rectangle.
        Args:
            width (int): Width of Rectangle. Value will be 0 if not specified.
            height (int): Height of Rectangle Value will be 0 if not specified.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Function that retrieves width of Rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Function that sets the value of the width of a Rectangle:
        Args:
            value (int): Value for the width. Must be int >= 0.
        Raises:
            TypeError: must be integer
            ValueError: muist be >= 0
        """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Function that retrieves the height of a Rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Function that sets the height of a Rectangle
        Args:
            value (int): Value of the height. Must be int >= 0
        Raises:
            TypeError: must be an integer
            ValueError: must be >= 0
        """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Function that returns the area of a Rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Function that returns the perimeter of a Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
