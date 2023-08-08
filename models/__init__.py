#!/usr/bin/python3
"""The magic init file that turns a dir to a package"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
