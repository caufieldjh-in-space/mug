"""Address"""

import sys
import uuid
from random import choice, randint

from mug.constants import CONSONANTS, VOWELS
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
        # faddressee = f'{contents["addressee"]["description"]}'
        faddressee = f'{contents["addressee"]}'
    else:
        faddressee = ""
    if contents["address_number"]:
        if len(contents["address_number"]) == 1:
            faddress_number = f'{contents["address_number"][0]}'
        else:
            faddress_number = "\n".join(contents["address_number"])
    else:
        faddress_number = ""
    if contents["street"]:
        fstreet = " ".join(contents["street"])
    else:
        fstreet = ""
    if contents["locality"]:
        flocality = f'{contents["locality"]}'
    else:
        flocality = ""
    contents["description"] = f"{faddressee}\n{faddress_number} {fstreet}\n{flocality}"

    contents["name"] = f"{faddress_number} {fstreet}"

    return contents


def addressee():
    # TODO: generate Person object
    return "Placeholder Placeholder"


def address_number():

    address_number = []
    if randint(0, 19) == 0:
        modnumber = str(randint(1, 99))
        if randint(0, 19) == 0:
            modnumber = modnumber + str(choice(choice([CONSONANTS, VOWELS]))).upper()
        add_mod = sample_res("address_modifier")["id"][0]
        address_number.append(f"{add_mod} {modnumber}")
    main_num = str(randint(1, 9999)) # TODO: set this so it is usually a lower number
    address_number.append(main_num)

    return address_number


def street():
    # TODO: title case in case there are lowercase first characters
    # TODO: generic highways
    # TODO: two-named streets
    # TODO: simple modifiers e.g. "green hill"
    street_postfix = sample_res("street_postfix")["id"][0]
    if randint(0, 9) == 0:
        street_name = choice(["Hwy", "Rte"])
        another_number = randint(1,99)
        street = [f"{street_name} {another_number}"]
    else:
        street_name = sample_res(
            choice(["english_word", "familyname", "givenname"])
    )["id"][0]
        street = [street_name, street_postfix]
    return street


def locality():
    return "placeholder town, PA 19341"
