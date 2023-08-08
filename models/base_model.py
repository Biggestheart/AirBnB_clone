#!/usr/bin/python3
"""This module contains the base class for the AirBnB clone"""
import uuid, datetime

class BaseModel():
    """Defines all the attributes and methods shared in the program"""

    def __init__(self):
        """Initializing the class"""
        self.id = str(uuid.uuid4()) # getting a random uuid for id
        # setting the dates to the current date
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """returns a str representation of the object"""
        class_name = self.__class__.__name__ # getting the class name
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dict of key/value pairs of the __dict__ instance"""
        the_dict = self.__dict__.copy()
        the_dict["__class__"] = self.__class__.__name__
        the_dict["created_at"] = self.created_at.isoformat()
        the_dict["updated_at"] = self.updated_at.isoformat()
        return the_dict
