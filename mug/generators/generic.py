"""generic.py - defines the basic MUGProduct class"""

import uuid

class MUGProduct:
    """ Parent class of all MUG generated objects."""

    def __init__(self):
        """Init - assign a unique ID"""
        self.id = str(uuid.uuid4())