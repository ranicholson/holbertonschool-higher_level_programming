#!/usr/bin/python3


def divisible_by_2(my_list=[]):

    if len(my_list) == 0:
        nlist = []
        return nlist

    nlist = my_list.copy()

    for x in my_list:
        if x % 2 == 0:
            nlist[x] = True

        else:
            nlist[x] = False

    return nlist
