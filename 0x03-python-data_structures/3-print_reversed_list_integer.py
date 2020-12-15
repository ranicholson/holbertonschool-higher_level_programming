#!/usr/bin/bash


def print_reversed_list_integer(my_list=[]):

    x = 0
    y = len(my_list)

    while len(my_list) - x != 0:

        print("{:d}".format(my_list[(y - 1)]))
        y -= 1
        x += 1
