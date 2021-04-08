#!/usr/bin/python3
"""Function to find peak"""


def find_peak(list_of_integers):
    """Finds peak in unsorted list"""

    if list_of_integers == []:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        return max(list_of_integers)

    loi = list_of_integers
    begin = 0
    end = len(list_of_integers) - 1
    middle = int(len(list_of_integers) / 2)

    if loi[middle] > loi[middle + 1] and loi[middle] > loi[middle - 1]:
        return loi[middle]
    elif loi[middle] < loi[middle - 1]:
        end = middle - 1
        loi = list_of_integers[0:end]
        return find_peak(loi)
    else:
        begin = middle + 1
        loi = list_of_integers[begin:]
        return find_peak(loi)
