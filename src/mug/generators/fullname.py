"""FullName"""

from random import randint
import sys
import uuid

from mug.load_class import get_class_details
from mug.load_data import sample_res

GEN_NAME = "FullName"
GEN_MOD = sys.modules[__name__]


def generate():
    contents = {}

    details = get_class_details(GEN_NAME)
    print(details)

    for slot in details:
        if slot == "id":
            contents[slot] = str(uuid.uuid4())
        else:
            gen_func = getattr(GEN_MOD, slot)
            contents[slot] = gen_func()

    contents[
        "name"
    ] = f'{contents["title"][0]} {contents["given_name"][0]} \'{contents["preferred_name"][0]}\' {contents["other_name"][0]} {contents["family_name"][0]} {contents["suffix"][0]}'

    return contents


def given_name():
    return sample_res("givenname")["id"]


def family_name():
    return sample_res("familyname")["id"]


def other_name():
    if randint(0, 9) > 0:
        return sample_res("givenname")["id"]
    else:
        return " "


def preferred_name():
    # TODO: make this aware of what given_name uses
    #       otherwise it's nonsensical
    if randint(0, 9) > 5:
        return sample_res("givenname")["nickname"]
    else:
        return " "


def title():
    if randint(0, 9) > 8:
        return sample_res("prenomtitle")["full_title"]
    else:
        return " "


def suffix():
    if randint(0, 9) > 8:
        return sample_res("namesuffix")["id"]
    else:
        return " "
