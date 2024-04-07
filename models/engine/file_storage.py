#!/usr/bin/python3
""" This module defines storage """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class for file storage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This function represents all"""
        return self.__objects

    def new(self, obj):
        """This function represents new"""
        if obj:
            keyequal = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[keyequal] = obj

    def save(self):
        """This function represents save"""
        json_dict = {}
        for k, v in FileStorage.__objects.items():
            json_dict[k] = v.to_dict()
        with open(FileStorage.__file_path, 'w') as filejson:
            json.dump(json_dict, filejson, indent=4)

    def reload(self):
        """This function represents reload"""
        try:
            with open(FileStorage.__file_path, 'r') as filejsonload:
                dict_load = json.load(filejsonload)
                for k, v in dict_load.items():
                    FileStorage.__objects[k] = eval(v["__class__"])(**v)
        except FileNotFoundError:
            return
