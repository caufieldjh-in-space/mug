"""generic.py - defines the basic MUGProduct class"""

import uuid

class MUGProduct:
    """ Parent class of all MUG generated objects."""

    # TODO: add fantasy place generator
    # TODO: add tech co generator (as child of Company)

    def __init__(self):
        """Init - assign a unique ID"""
        self.id = str(uuid.uuid4())