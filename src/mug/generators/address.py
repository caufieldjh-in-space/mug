"""Address"""

import sys
import uuid
from random import choice, randint

from mug.constants import CONSONANTS, VOWELS
from mug.generators import fullname
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
        faddressee = f'{contents["addressee"]["description"]}'
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
        flocality = " ".join(contents["locality"])
    else:
        flocality = ""
    contents["description"] = f"{faddressee}\n{faddress_number} {fstreet}\n{flocality}"

    contents["name"] = f"{faddress_number} {fstreet}"

    return contents


def addressee():
    # TODO: generate Person object instead of FullName
    #       or reconsider this in the model
    # TODO: Add another name rendering to FullName
    #       that's somewhere between the current name and desc
    return fullname.generate()


def address_number():
    address_number = []
    if randint(0, 19) == 0:
        modnumber = str(randint(1, 99))
        if randint(0, 19) == 0:
            modnumber = modnumber + str(choice(choice([CONSONANTS, VOWELS]))).upper()
        add_mod = sample_res("address_modifier")["id"][0]
        address_number.append(f"{add_mod} {modnumber}")
    if randint(0,1) == 0:
        main_num = str(randint(0,99))
    else:
        main_num = str(randint(1, randint(1,9999)))
    address_number.append(main_num)

    return address_number

def street():
    street_postfix = sample_res("street_postfix")["id"][0]
    if randint(0, 9) == 0:
        street_name = choice(["Hwy", "Rte"])
        another_number = randint(1, 99)
        street = [f"{street_name} {another_number}"]
    else:
        street_name = sample_res(choice(["english_word", "familyname", "givenname"]))[
            "id"
        ][0]
        if randint(0, 9) == 0:
            street_prefix = sample_res("placeprefix")["id"][0]
            street = [street_prefix, street_name.title(), street_postfix]
        elif randint(0, 9) == 0:
            street_prefix = sample_res("genericplace")["id"][0]
            street = [street_name.title(), street_prefix.title(), street_postfix]
        else:
            street = [street_name.title(), street_postfix]
    return street


def locality():
    # Localities selected from simplemaps - see https://simplemaps.com/data/us-zips
    place = sample_res("us_place")
    area = place['id'][0]
    state_abbrev = place['state_abbreviation'][0]
    zipcode = str(place['zipcode'][0])
    locality = [area, state_abbrev, zipcode]
    return locality
