#!/usr/bin/env python3
import json
from models.base_model import BaseModel
""" A module containing a single class for serialisation/deserialisation
    Class: FileStorage
"""
class FileStorage:
    """ Serialiser/deserialiser
        -Args:
            -__file_path: The path to JSON file
            -__objects: The dictionary representation of the obj
        -Methods:
            -all(self): Get all the objects
            -new(self): set in __objects the obj
            -save(self): serialises __objects to JSON
            -reload(self): deserialises JSON to __objects
    """
    def __init__(self):
        """ Class constructor """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """ Geting all the objects of the class """
        return self.__objects

    def new(self, obj):
        """ Creating new object by adding it to the list of objects 
            Args:
                -obj: The object to create
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """ Saving obj to a file """
        obj_dict = {}
        for k,v in self.__objects.items():
            obj_dict[k] = v.to_dict()

        with open(self.__file_path, "w") as wr:
                json.dump(obj_dict, wr)

    def reload(self):
        """ Get the json data """
        data = ""
        try:
            data = open(self.__file_path, "r")
            obj_dict = json.load(data)
            for k,v in obj_dict.items():
                obj = BaseModel(**v)
                self.__objects[k] = obj
            data.close()
        except IOError:
            pass
