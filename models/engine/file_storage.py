#!/usr/bin/python3
"""
Module containing the FileStorage class
"""
import json
import os
from datetime import datetime
from models.base_model import BaseModel


class FileStorage:
    """
    FileStorage class for serializing instances to JSON file
    and deserializing JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns the dictionary __objects

        Returns:
            dict: Dictionary of all objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id

        Args:
            obj: Object to be set in __objects
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists)
        """
        try:
            with open(self.__file_path, 'r') as file:
                loaded_objects = json.load(file)
                for key, value in loaded_objects.items():
                    class_name, obj_id = key.split('.')
                    value['created_at'] = datetime.strptime(
                        value['created_at'], "%Y-%m-%dT%H:%M:%S.%f"
                    )
                    value['updated_at'] = datetime.strptime(
                        value['updated_at'], "%Y-%m-%dT%H:%M:%S.%f"
                    )
                    obj_instance = eval(class_name)(**value)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass