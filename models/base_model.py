#!/usr/bin/python3
"""This module contains the base class for the AirBnB clone"""
import uuid
import datetime
from models import storage


class BaseModel():
    """Defines all the attributes and methods shared in the program"""

    def __init__(self, *args, **kwargs):
        """Initializing the class"""
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    # strptime creates a datetime obj from a str repr of date
                    # creating datetime from the dict value string
                    # created_at and updated_at
                    self.__dict__["created_at"] = datetime.datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())  # getting a random uuid for id
            # setting the dates to the current date
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)  # adding a call to the method new(self)

    def __str__(self):
        """returns a str representation of the object"""
        class_name = self.__class__.__name__  # getting the class name
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()
        storage.save()  # calling save method on storage from models/__init__

    def to_dict(self):
        """Returns a dict of key/value pairs of the __dict__ instance"""
        the_dict = self.__dict__.copy()  # creating a copy of __dict__
        # Storing values like classname, created_at and updated_at
        the_dict["__class__"] = self.__class__.__name__
        the_dict["created_at"] = self.created_at.isoformat()
        the_dict["updated_at"] = self.updated_at.isoformat()
        return the_dict
