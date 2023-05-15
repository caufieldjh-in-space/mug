"""CompanyName"""

import sys
import uuid
from random import choice, randint

from mug.load_class import get_class_details
from mug.load_data import sample_res
from mug.utils.textgen import make_acronym
from mug.utils.vary_text import all_upper, controlled_misspell, uncontrolled_misspell

GEN_NAME = "CompanyName"
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

    if contents["company_name_suffix"]:
        fsuffix = " ".join(contents["company_name_suffix"])

    if contents["company_name_main"]:
        fcompany_name_main = " ".join(contents["company_name_main"])
        contents["description"] = f"{fcompany_name_main} {fsuffix}"
        contents["name"] = contents["company_name_main"][0]

    return contents

# TODO: add portmanteaus, though that may mean adding a function
#       to get lists of many ids at once
# TODO: include some generic company names like TriState or General
# TODO: add some more Weirdness
def company_name_main():
    tc = randint(0, 2)
    if tc == 0:  # Acronym
        name = make_acronym()
    elif tc == 1:  # Simple word or phrase
        name = sample_res(
            choice(
                [
                    "animal",
                    "english_word",
                    "familyname",
                    "fictionalbeast",
                    "fictionalcharacter",
                    "givenname",
                    "latinword",
                ]
            )
        )["id"][0].title()
    elif tc == 2:  # Person names
        name1 = sample_res("familyname")["id"][0]
        name2 = sample_res("familyname")["id"][0]
        conn1 = choice(["", " ", ", "])
        name = f"{name1}{conn1}{name2}"
        if randint(0, 3) == 0:
            name3 = sample_res("familyname")["id"][0]
            conn2 = choice(["", "-", " & ", " + ", " And "])
            name = f"{name}{conn2}{name3}"

    # Modifiers
    # TODO: fix up this first modifier, it isn't quite right
    if randint(0, 6) == 0:
        postfix = sample_res(choice(["company_postfix_casual", "genericplace"]))["id"][0]
        conn = choice(["", " "])
        name = f"{name}{conn}{postfix}"
    if randint(0, 8) == 0:
        name = name.replace(" ", "")
    if randint(0, 6) == 0:
        name = controlled_misspell(name)
    if randint(0, 6) == 0:
        name = uncontrolled_misspell(name)
    if randint(0, 9) == 0:
        name = all_upper(name)


    return [name]

# TODO: tune this up a bit as sometimes it generates very strange combos
#       Maybe use just one business/industry type and just one postfix?
def company_name_suffix():
    suffixes = []
    used_already = []
    for i in range(randint(1, 2)):
        this_choice = choice(
            [
                "businesstype",
                "company_postfix_formal",
                "industry",
            ]
        )
        if this_choice not in used_already:
            suffixes.append(sample_res(this_choice)["id"][0])
        used_already.append(this_choice)
    return suffixes
