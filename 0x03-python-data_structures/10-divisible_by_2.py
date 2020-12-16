#!/usr/bin/python3


def divisible_by_2(my_list=[]):

    nlist = my_list.copy()

    for x in nlist[:]:
        if x % 2 == 0 and x != 0:
            nlist[x] = True

        else:
            nlist[x] = False

    return nlist
