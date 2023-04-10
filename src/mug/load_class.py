"""Dynamically load a class from the MUG Python datamodel."""

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