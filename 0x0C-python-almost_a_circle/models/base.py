#!/usr/bin/python3

"""Class Base definition"""
import json


class Base:
    """Base class for other classes in project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializer for Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method that returns JSON string representation of dictionary"""
        if list_dictionaries is None or list_dictionaries == {}:
            return ("[]")
        else:
            return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string to files"""
        file = cls.__name__ + ".json"
        with open(file, "w") as ofile:
            if list_objs is None:
                ofile.write("[]")
            else:
                ndic = []
                for x in list_objs:
                    ndic.append(x.to_dictionary())
                ofile.write(Base.to_json_string(ndic))
