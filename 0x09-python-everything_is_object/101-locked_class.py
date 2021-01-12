#!/usr/bin/python3

"""Locked class that can only be called by first_name"""


class LockedClass:
    """Class that only has attribute first_name"""

    __slots__ = ["first_name"]
