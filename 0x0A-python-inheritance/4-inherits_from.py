#!/usr/bin/python3


"""Function that returns true if object is an instance of an object inherited
from the specified class"""


def inherits_from(obj, a_class):
    """Function that checks if the object is a class that has inheritance
    from the specified class.
    Args:
        obj (obj): object to check
        a_class (class): class to check object
    Return:
        True: if it is true
        False: if it is false
    """

    if issubclass(type(obj), a_class) is True and type(obj) != a_class:
        return (True)
    else:
        return (False)
