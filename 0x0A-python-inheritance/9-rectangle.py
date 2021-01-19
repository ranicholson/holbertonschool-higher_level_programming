#!/usr/bin/python3

""" Defining Rectangle a subclass of BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Method of instantiation for rectangle
        Args:
            width (int): must be an int larger than 0
            height (int): must be an int larger than 0
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Method that returns area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Returns description of the rectangle"""
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
