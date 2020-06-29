#!/usr/bin/python3

""" Module of Base for AirBnB clone project
"""
from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel:
    """
    Class BaseModel defines all common attributes/methods
    for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Instantiation method or constructor with *args and **kwargs
        """
        for key, value in kwargs.items():
            if key == "__class__":
                continue

            if (key == "created_at" or key == "updated_at"):
                value = datetime.now()

            setattr(self, key, value)

        if "id" not in kwargs.keys():
            self.id = str(uuid4())

        if "created_at" not in kwargs.keys():
            self.created_at = datetime.now()

        if "updated_at" not in kwargs.keys():
            self.updated_at = datetime.now()

        if len(kwargs) == 0:
            storage.new(self)

    def save(self):
        """
        updates the public instance updated_at attribute
        with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        var_dict = self.__dict__.copy()
        #print("$$$$$$$$\n\n",var_dict, "\n\n\n")
        var_dict["__class__"] = self.__class__.__name__
        var_dict["created_at"] = self.created_at.isoformat()
        var_dict["updated_at"] = self.updated_at.isoformat()
        #print("****\n\n",var_dict, "\n\n\n")
        return var_dict

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>
        """
        print_ = "[{}] ({}) {}"
        return print_.format(self.__class__.__name__, self.id, self.__dict__)
