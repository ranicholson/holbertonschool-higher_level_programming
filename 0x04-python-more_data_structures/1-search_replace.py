#!/usr/bin/python3


def search_replace(my_list, search, replace):

    return list(map(lambda x: x if x != search else (x*0) + replace, my_list))
