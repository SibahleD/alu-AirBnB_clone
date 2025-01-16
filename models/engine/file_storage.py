#!/usr/bin/python3
"""
This class defines all common attributes/methods for other classes.
Attributes:
    _file_path (str): path to the JSON file.
    __objects: (dict): Stores all objects by <class name>.id
    updated_at (datetime): The datetime when the instance was last updated.
Methods:
    all(): returns the dictionary __objects
    new(obj): sets in __objects the obj with key.
    save():  serializes __objects to the JSON file.
    reload(): deserializes the JSON file to __objects
"""

import json
import os 

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (if it exists)"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = key.split('.')[0]
                    self.__objects[key] = eval(class_name)(**value)