#!/usr/bin/python3
"""
Initialization models_package
"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
