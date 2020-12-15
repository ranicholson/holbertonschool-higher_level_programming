#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    if matrix is not None:
        y = 0
        for x in matrix:
            for y in x:
                print("{:d} ".format(y), end="")
            if y == (len(matrix) - 1):
                print()
            else:
                print(" ")
                y += 1
