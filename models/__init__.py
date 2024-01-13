#!/usr/bin/python3
"""
__init__.py: Package initializer

Description:
    - Initializes the package with a FileStorage instance
    from the models.engine module.
    - It triggers a reload operation, loading existing data
    from file.json into memory.
"""


from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
