#!/usr/bin/python3

"""Subclass Rectangle inherits from Base class"""


class Rectangle(Base):
    """Rectangle that inherits from class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializer method of class Rectanlge
        Args:
            width (int): width of Rectangle
            height (int): height of Rectangle
            x ():
            y ():
            id (int):ID number of rectangle
        """
        super().init(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """Retrieve the width of Rectangle"""
            return (self.__width)

        @width.setter
        def width(self, width) def width(self, value):
        """Function that sets the width of a Rectangle:
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

    @property
    def x(self):
        """Function that retrieves the height of a Rectangle"""
        return (self.__x)

    @height.setter
    def x(self, value):
        """Function that sets the height of a Rectangle
        Args:
            value (int): Must be int > 0
        Raises:
            TypeError: must be an integer
            ValueError: must be > 0
        """
        if isinstance(value, int) is False:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Function that retrieves the height of a Rectangle"""
        return (self.__y)

    @height.setter
    def height(self, value):
        """Function that sets the height of a Rectangle
        Args:
            value (int): Must be int >= 0
        Raises:
            TypeError: must be an integer
            ValueError: must be >= 0
        """
        if isinstance(value, int) is False:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
