"""FullName"""

from random import randint, choice
import sys
import uuid

from mug.generators import nickname
from mug.load_class import get_class_details
from mug.load_data import sample_res


GEN_NAME = "FullName"
GEN_MOD = sys.modules[__name__]

# TODO: Enable setting first and/or middle name to initial
# TODO: add preferred pronouns - this will need to go in schema too
#       and it's a tricky one, involving some Judgement

def generate():
    contents = {}

    details = get_class_details(GEN_NAME)
    # print(details)

    for slot in details:
        if slot == "id":
            contents[slot] = str(uuid.uuid4())
        elif slot == "preferred_name":
            gen_func = getattr(GEN_MOD, slot)
            contents[slot] = gen_func(contents)
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
        fpreferred_name = (
            f'\'{contents["preferred_name"][0]}\' '
        )
    else:
        fpreferred_name = ""
    if contents["other_name"]:
        fother_name = f'{" ".join(contents["other_name"])} '
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

    if contents["preferred_name"]:
        contents["name"] = contents["preferred_name"][0]
    else:
        contents["name"] = contents["given_name"][0]

    return contents


def given_name():
    return sample_res("givenname")["id"]


def family_name():
    if randint(0, 9) > 1:
        return sample_res("familyname")["id"]
    else:
        hyphenate = [
            "-".join(
                [sample_res("familyname")["id"][0], sample_res("familyname")["id"][0]]
            )
        ]
        return hyphenate


def other_name():
    if randint(0, 9) > 0:
        name = choice([sample_res("givenname")["id"], sample_res("familyname")["id"]])
        if randint(0, 9) == 0:
            name.extend(
                choice([sample_res("givenname")["id"], sample_res("familyname")["id"]])
            )
        return name
    else:
        return None


def preferred_name(names):
    if randint(0, 9) > 6:
        big_names = [names["given_name"][0], names["family_name"][0]]
        return nickname.generate(big_names)
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
