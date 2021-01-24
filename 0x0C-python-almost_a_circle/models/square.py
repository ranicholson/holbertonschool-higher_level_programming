#!/usr/bin/python3

"""Class Square that inherits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class than inherits from Rectangle which inherits from Base"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializer for Square class
        Args:
            size (int): size of Square
            x (int):
            y (int):
            id (int):ID number of Square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string with rectangle description"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                  self.width))

    @property
    def size(self):
        """Retrieve the size of Square"""
        return (self.width)

    @size.setter
    def size(self, size):
        """Sets the size of square"""
        self.width = size
        self.height = size
