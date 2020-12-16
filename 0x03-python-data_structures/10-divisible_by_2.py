#!/usr/bin/python3


def divisible_by_2(my_list=[]):

    if len(my_list) == 0:
        return None
    nlist = my_list.copy()
    x = 0
    for x in nlist:
        if x % 2 == 0 and x != 0:
            nlist[x] = True

        else:
            nlist[x] = False

    return nlist
