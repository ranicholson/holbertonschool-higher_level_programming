#!/usr/bin/python3


def multiple_returns(sentence):

    if len(sentence) == 0:
        multup = (0, "None")
        return multup

    multup = (len(sentence), sentence[0])

    return multup
