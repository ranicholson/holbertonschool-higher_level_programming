#!/usr/bin/python3

"""Function that returns true if the object is exactly an instance of the
specified class"""


def is_same_class(obj, a_class):
    """Function that returns true/false comparing object to class
    Args:
        obj (obj): object to compare against class
        a_class (class): class to compare object against
    Return:
        True: if the object is the exact same as the class
        Fals: if the object is not a match to the class
    """

    if type(obj) == a_class:
        return (True)
    else:
        return False
