#!/usr/bin/python3

"""Defining subclass MyList from super class list"""


class MyList(list):
    """ Subclass that inherits from list"""

    def print_sorted(self):
        """Prints sorted list"""
        print(sorted(self))
