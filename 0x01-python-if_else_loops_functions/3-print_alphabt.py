#!/usr/bin/python3

for count in range(97, 123):
    if count == 101 or count == 113:
        continue
    print("{:c}".format(count), end="")
