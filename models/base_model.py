#!/usr/bin/python3
"""
This class defines all common attributes/methods for other classes.
Attributes:
    id (str): Unique identifier for each instance.
    created_at (datetime): The datetime when the instance was created.
    updated_at (datetime): The datetime when the instance was last updated.
Methods:
    __init__(): Initializes a new instance of BaseModel.
    __str__(): Returns a string representation of the instance.
    save(): Updates the 'updated_at' attribute with the current datetime.
    to_dict(): Returns a dictionary containing all keys/values of the instance.
"""
import uuid
from datetime import datetime
from models import FileStorage

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            FileStorage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}), {self.__dict__}" 

    def save(self):
        self.updated_at = datetime.now()
        FileStorage.save()

    def to_dict(self):
        dict_rep = self.__dict__.copy()
        dict_rep["created_at"] = self.created_at.isoformat()
        dict_rep["updated_at"] = self.updated_at.isoformat()
        dict_rep["__class__"] = self.__class__.__name__
        return dict_rep