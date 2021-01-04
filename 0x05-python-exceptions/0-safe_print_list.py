#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):

    for y in range(x):
        try:
            print("{}".format(my_list[y]), end="")

        except IndexError:
            y -= 1
            break

    print()

    return (y + 1)
