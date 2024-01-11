#!/usr/bin/python3
"""
Module containing the BaseModel class
"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """
    BaseModel class that defines common attributes/methods
    for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel

        Args:
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    if isinstance(value, str):
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the object

        Returns:
            str: String representation of the object
        """
        return "[{}] ({}) {}".format(
                                    self.__class__.__name__,
                                    self.id,
                                    self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance

        Returns:
            dict: Dictionary representation of the object
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
