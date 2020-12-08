#!/usr/bin/python3

for x in range (0, 10):
    for y in range (1, 10):
        if (y - x) <= 0:
            continue
        elif y == 9 and x == 8:
            print("{:d}{:d}".format(x, y))
            break
        else:
            print("{:d}{:d}".format(x, y), end=", ")
