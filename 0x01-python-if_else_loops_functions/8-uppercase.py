#!/usr/bin/python3


def uppercase(str):

    for x in str:
        y = ord(x)
        if y >= 97 and y <= 122:
            y = chr(y - 32)
            print("{}".format(y), end="")

        else:
            print("{}".format(x), end="")

    print()
