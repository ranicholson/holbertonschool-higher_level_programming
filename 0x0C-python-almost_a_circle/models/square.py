#!/usr/bin/python3

"""Class Square that inherits from Rectangle"""

from rectangle import Rectangle


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

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        pos = 0
        if args is not None and len(args) > 0:
            for arg in args:
                if pos == 0:
                    self.id = arg
                elif pos == 1:
                    self.width = arg
                    self.height = arg
                elif pos == 2:
                    self.x = arg
                elif pos == 3:
                    self.y = arg
                pos += 1
        elif kwargs is not None and len(kwargs) > 0:
            for key, arg in kwargs.items():
                if key == "id":
                    self.id = arg
                elif key == "size":
                    self.width = arg
                    self.height = arg
                elif key == "x":
                    self.x = arg
                elif key == "y":
                    self.y = arg

    def to_dictionary(self):
        """Returns dictionary representation"""
        return ({"id": self.id, "size": self.width, "x": self.x, "y": self.y})
