#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    if matrix is not None:
        for x in matrix:
            for y in x:
                print("{:d} ".format(y), end="")
            print()
