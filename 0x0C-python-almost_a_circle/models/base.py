#!/usr/bin/python3

"""Class Base definition"""


class Base:
    """Base class for other classes in project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializer for Base class"""
        if id == None:
            self.id = None
        else:
            __nb_objects += 1
            self.id = __nb_objects
