#!/usr/bin/python3

"""Function to print a dquare using #"""


def print_square(size):

    """ Function to print square.
    Args:
        size (int): size of the square
    Raises:
        TypeError: Size must be an int
        ValueError: Size must be >= 0
    Return: None
    """

    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        print("{}".format(size * "#"))
