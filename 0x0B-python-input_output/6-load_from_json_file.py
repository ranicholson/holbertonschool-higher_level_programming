#!/usr/bin/python3

"""Function that creates object from JSON file"""
import json


def load_from_json_file(filename):
    """Creat obj from json file"""
    with open(filename) as file:
        return (json.load(file))
