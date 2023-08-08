#!/usr/bin/python3
"""This module is to store data to a file"""
import json
import os


class FileStorage():
    """This class is for storing the data into a file"""

    # private class attributes
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets obj in the __objects"""
        key = obj.__class__.__name__
        FileStorage.__objects["{} {}".format(key, obj.id)] = obj

    def save(self):
        """serializes __objects to the file_path"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as doc:
            dic = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(dic, doc)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        # checking if the file exists
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as doc:
                the_dict = json.load(doc)
            # storing the parsed json to the __object variable
            FileStorage.__objects = the_dict
        else:
            return
