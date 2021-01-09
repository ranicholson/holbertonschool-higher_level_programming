#!/usr/bin/python3

"""Function that divides all elements of a matrix"""


def matrix_divided(matrix, div):

    """Divide elements of a matrix
    Args:
        matrix (list): matrix of elements to divide
        div (int/float): integer to divide elements by
    Raises:
        TypeError: Occurs if elements of the matrix or div are not integers or
            floats.Also occurs if rows of the matrix are not the same size.
        ZeroDivisionError: Occurs when div is 0
    Return: New matrix with values of each element divided by div.
    """

    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    if isinstance(div, (float, int)) is False or div == 0:
        if div == 0:
            raise ZeroDivisionError("division by zero")
        else:
            raise TypeError("div must be a number")

    nlist = []
    clist = []
    rowlen = len(matrix[0])

    for x in matrix:
        if len(x) != rowlen:
            raise TypeError("Each row of the matrix must have the same size")
        for y in x:
            if isinstance(y, (int, float)) is False:
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
            nlist.append(round((y / div), 2))
        rowlen = len(x)
        clist.append(nlist)
        nlist = []

    return (clist)
