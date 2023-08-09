#!/usr/bin/python3
"""
This module_holds the class_User
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Implemenatation_of the class_User
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
