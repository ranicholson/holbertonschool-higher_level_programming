#!/usr/bin/python3


def no_c(my_string):

    nstring = ""

    for x in my_string:

        if x == 'c' or x == 'C':
            continue

        nstring += x

    return nstring
