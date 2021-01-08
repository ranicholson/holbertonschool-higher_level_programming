#!/usr/bin/python3

"""Function to add two integers"""


def add_integer(a, b=98):

    """Returns the sum of two integers.

    Accepts float as well, but must be converted to int.
    Args:
        a (int/float): first argument
        b (int/float): second argument
    Return:
        Sum of a + b
    Raises:
        TypeError: Occurs if a or b is an integer or float.
    """

    if isinstance(a, int) is False:
        if isinstance(a, float) is True:
            a = int(a)

        else:
            raise TypeError("a must be an integer")

    if isinstance(b, int) is False:
        if isinstance(b, float) is True:
            b = int(b)

        else:
            raise TypeError("b must be an integer")

    return (a + b)
