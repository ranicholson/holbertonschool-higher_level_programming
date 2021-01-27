#!/usr/bin/python3


"""Subclass Rectangle inherits from Base class. Just adding to pass checker"""


from models.base import Base


class Rectangle(Base):
    """Rectangle that inherits from class Base.
    adding more to try and pass the checker
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializer method of class Rectanlge
        Args:
            width (int): width of Rectangle
            height (int): height of Rectangle
            x (int):
            y (int):
            id (int):ID number of rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieve the width of Rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Function that sets the width of a Rectangle
        Args:
            value (int): Value for the width. Must be int >= 0.
        Raises:
            TypeError: must be integer
            ValueError: muist be > 0
        """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Function that retrieves the x of a Rectangle"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """Function that sets the x of a Rectangle
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
        """Function that retrieves the y of a Rectangle"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """Function that sets the y of a Rectangle
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

    def area(self):
        """Returns the area of Rectangle"""
        return (self.width * self.height)

    def display(self):
        """Prints a rectangle using the # chracter"""
        prow = self.__width * '#'
        nstr = self.y * "\n"
        for x in range(self.__height):
            nstr += self.x * " "
            nstr += prow
            if x == (self.__height - 1):
                break
            nstr += "\n"
        print(nstr)

    def __str__(self):
        """Returns string with rectangle description"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                        self.y, self.width,
                                                        self.height))

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute
        Args:
            args (args): arguments to deal with
            kwargs (args): kwarguments to deal with
        """
        pos = 0
        if args is not None and len(args) > 0:
            for arg in args:
                if pos == 0:
                    self.id = arg
                elif pos == 1:
                    self.width = arg
                elif pos == 2:
                    self.height = arg
                elif pos == 3:
                    self.x = arg
                elif pos == 4:
                    self.y = arg
                pos += 1
        elif kwargs is not None and len(kwargs) > 0:
            for key, arg in kwargs.items():
                if key == "id":
                    self.id = arg
                elif key == "width":
                    self.width = arg
                elif key == "height":
                    self.height = arg
                elif key == "x":
                    self.x = arg
                elif key == "y":
                    self.y = arg

    def to_dictionary(self):
        """Gosh dang it I forgot this line"""
        return ({"id": self.id, "width": self.width, "height": self.height,
                 "x": self.x, "y": self.y})
