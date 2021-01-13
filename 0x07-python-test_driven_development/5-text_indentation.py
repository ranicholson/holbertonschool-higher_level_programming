#!/usr/bin/python3

"""Function that inserts two lines after ., ?, or :"""


def text_indentation(text):

    """Function to print two lines after specified characters.
    Args:
        text (str): text to print
    Raises:
        TypeError: Raised if anything other than a string is passed
    Return: None
    """

    y = 0

    if isinstance(text, str) is False:
        raise TypeError("text must be a string")

    for x in text:
        if x == " " and y == 1:
            y = 0
            continue

        print(x, end="")
        if x == "." or x == "?" or x == ":":
            print("\n")
            y = 1
