#!/usr/bin/python3

count = 0

while count <= 99:
    if count != 99:
        print("{:02}".format(count), end=(", "))
    else:
        print("99")

    count += 1
