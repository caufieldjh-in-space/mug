"""Dynamically load a class from the MUG Python datamodel."""

import importlib

from mug_schemas.datamodel.mug_schemas import NamedThing

def load_class(classname: str):
    """Load class from the MUG Python datamodel."""

    return NamedThing