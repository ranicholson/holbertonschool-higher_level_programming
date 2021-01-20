#!/usr/bin/python3

"""Define Square subclass with inheritance from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Methods and attributes of the Square class"""

    def __init__(self, size):
        """Method to initialize new object in the Square class
        Args: size (int): size of Square to create
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
