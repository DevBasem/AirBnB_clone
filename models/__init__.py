#!/usr/bin/python3
"""
Module to initialize the package.
"""
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
