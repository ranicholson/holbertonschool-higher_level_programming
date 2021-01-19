#!/usr/bin/python3

"""Function that returns available attributes and methods of an object"""


def lookup(obj):
    """Functio to list attributes and methods of an object.
    Args: obj (obj): object to look at
    Return: List object containing results
    """

    return (dir(obj))
