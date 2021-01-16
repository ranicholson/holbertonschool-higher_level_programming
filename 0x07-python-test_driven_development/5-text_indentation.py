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
    pstr = ""

    if isinstance(text, str) is False:
        raise TypeError("text must be a string")

    while y < len(text):
        pstr += text[y]
        if text[y] in ".?:":
            pstr += "\n\n"
            y += 1
            while text[y] == " ":
                y += 1
        else:
            y += 1
    print(pstr, end="")
