"""Address"""

from random import randint, choice
import sys
import uuid

from mug.load_class import get_class_details
from mug.load_data import sample_res


GEN_NAME = "Address"
GEN_MOD = sys.modules[__name__]

def generate():
    contents = {}

    details = get_class_details(GEN_NAME)

    for slot in details:
        if slot == "id":
            contents[slot] = str(uuid.uuid4())
        else:
            gen_func = getattr(GEN_MOD, slot)
            contents[slot] = gen_func()

    # Format for printing
    # TODO: make a small utility to do this
    # TODO: consider adding all to list and joining instead of managing spaces
    if contents["addressee"]:
        #faddressee = f'{contents["addressee"]["description"]}'
        faddressee = f'{contents["addressee"]}'
    else:
        faddressee = ""
    if contents["address_number"]:
        faddress_number = f'{contents["address_number"]}'
    else:
        faddress_number = ""
    if contents["street"]:
        fstreet = f'{contents["street"]}'
    else:
        fstreet = ""
    if contents["locality"]:
        flocality = f'{contents["locality"]}'
    else:
        flocality = ""
    contents[
        "description"
    ] = f'{faddressee}\n{faddress_number} {fstreet}\n{flocality}'


    contents["name"] = f'{faddress_number} {fstreet}'

    return contents


def addressee():
    # TODO: generate Person object
    return "Placeholder Placeholder"


def address_number():
    return randint(1,999)


def street():
    return "Street Road"


def locality():
    return "placeholder town, PA 19341"

