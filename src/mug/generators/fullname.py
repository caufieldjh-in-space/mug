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

    # Format for printing
    # TODO: make a small utility to do this
    # TODO: consider adding all to list and joining instead of managing spaces
    if contents["title"]:
        ftitle = f'{contents["title"][0]} '
    else:
        ftitle = ""
    fgiven_name = f'{contents["given_name"][0]} '
    if contents["preferred_name"]:
        fpreferred_name = f'\'{contents["preferred_name"][0]}\' '
    else:
        fpreferred_name = ""
    if contents["other_name"]:
        fother_name = f'{contents["other_name"][0]} '
    else:
        fother_name = ""
    ffamily_name = f'{contents["family_name"][0]}'
    if contents["suffix"]:
        fsuffix = f' {contents["suffix"][0]}'
    else:
        fsuffix = ""
    contents[
        "description"
    ] = f"{ftitle}{fgiven_name}{fpreferred_name}{fother_name}{ffamily_name}{fsuffix}"

    contents["name"] = f'{contents["given_name"][0]} {contents["family_name"][0]}'

    return contents


def given_name():
    return sample_res("givenname")["id"]


def family_name():
    if randint(0, 9) > 1:
        return sample_res("familyname")["id"]
    else:
        hyphenate = ["-".join(
            [sample_res("familyname")["id"][0], sample_res("familyname")["id"][0]]
        )]
        return hyphenate


def other_name():
    if randint(0, 9) > 0:
        return sample_res("givenname")["id"]
    else:
        return None


def preferred_name():
    # TODO: make this aware of what given_name uses
    #       otherwise it's nonsensical
    #       My gut feeling is to make this its own function
    #       so the nicks can be random, or related to the given name,
    #       or to the family name, or an initial, or a username
    if randint(0, 9) > 5:
        return sample_res("givenname")["nickname"]
    else:
        return None


def title():
    if randint(0, 9) > 8:
        return sample_res("prenomtitle")["full_title"]
    else:
        return None


def suffix():
    if randint(0, 9) > 8:
        return sample_res("namesuffix")["id"]
    else:
        return None
