#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):

    x = 0
    my_list.reverse()

    while len(my_list) - x != 0:

        print("{:d}".format(my_list[x]))
        x += 1
