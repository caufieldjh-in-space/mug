"""Dynamically load a class from the MUG Python datamodel."""

import importlib

from src.mug_schemas.datamodel.mug_schemas import NamedThing

def load_class(classname: str):
    """Load class from the MUG Python datamodel."""

    return NamedThing