#!/usr/bin/python3

"""Function that adds attribute to object"""


def add_attribute(mclass, aname, aval):
    """Function to add attribute
    Args:
        mclass (obj): object to add attribute to
        aname (str): name of attribute to add
        aval (str): attribute value to set
    """

    if hasattr(mclass, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(mclass, aname, aval)
