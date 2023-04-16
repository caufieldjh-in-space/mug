"""Dynamically load a class, or details about it, from the MUG Python datamodel."""

import importlib
import sys


def load_model_class(classname: str):
    """Load class from the MUG Python datamodel."""

    try:
        module = importlib.import_module("mug_schemas.datamodel.mug_schemas")
        selclass = getattr(module, classname)
    except AttributeError:
        sys.exit(f"Input class {classname} not found in schema.")

    return selclass


def load_generator_class(modname: str):
    """Load module and class from the generators."""

    modname = modname.lower()
    module = importlib.import_module(f"mug.generators.{modname}")
    selclass = getattr(module, "generate")

    return selclass


def get_class_details(classname: str):
    """Return slot names and their data types for a class."""

    # These attributes aren't useful for populating the class
    extras = [
        "_inherited_slots",
        "class_class_uri",
        "class_class_curie",
        "class_name",
        "class_model_uri",
    ]

    this_class = load_model_class(classname)
    annots = this_class.__annotations__
    details = dict([(k, v) for (k, v) in annots.items() if k not in extras])

    return details
