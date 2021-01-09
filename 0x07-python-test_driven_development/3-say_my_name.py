#!/usr/bin/python3

"""Function that prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):

    """ Function to print name.
    Args:
        first_name (string): first name to print. Required
        last_name (string): last name to print. Optional
    Raises:
        TypeError raised if anything other than strings are passed
    Return: None
    """

    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")

    if isinstance(last_name, str) is False and last_name != "":
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
