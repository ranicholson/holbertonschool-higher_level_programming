#!/usr/bin/python3

"""Function that returns True if the object is an instance of a subclass
or its superclass"""


def is_kind_of_class(obj, a_class):
    """Returns true/false after checking type of sub/super class
    Args:
        obj (obj): object to camper against class
        a_class (class): class to compare the object to
    Return:
        True: if the object is of the sub/super class
        False: if it is not a match
    """

    if isinstance(obj, a_class) is True:
        return (True)
    else:
        return (False)
