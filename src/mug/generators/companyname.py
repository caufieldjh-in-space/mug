"""CompanyName"""

import sys
import uuid
from random import choice, randint

from mug.load_class import get_class_details
from mug.load_data import load_res, sample_res
from mug.utils.portmanteau import make_portmanteau
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
        elif slot == "company_name_suffix":
            biztype = sample_res(choice(["businesstype","industry"]))["id"][0]
            contents[slot] = company_name_suffix(biztype)
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


# TODO: inherit industry from parent if present
# TODO: add some more Weirdness
# TODO: add some associated words to business types
#       like "Bakery" may have bread, cake, etc
# TODO: add Tech Names
def company_name_main():
    tc = randint(0, 3)
    if tc == 0:  # Simple word or phrase
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
    elif tc == 1:  # Person names
        name1 = sample_res("familyname")["id"][0]
        name2 = sample_res("familyname")["id"][0]
        conn1 = choice(["", " ", ", "])
        name = f"{name1}{conn1}{name2}"
        if randint(0, 3) == 0:
            name3 = sample_res("familyname")["id"][0]
            conn2 = choice(["", "-", " & ", " + ", " And "])
            name = f"{name}{conn2}{name3}"
    elif tc == 2:  # Generic names
        name = sample_res("genericcompanyname")["id"][0]
    elif tc == 3:  # Portmanteaus alone
        wordlist = (load_res("english_word")["id"]).to_list()
        name = make_portmanteau((wordlist, wordlist)).title()

    # Modifiers
    # TODO: fix up this first modifier, it isn't quite right
    if randint(0, 6) == 0:
        postfix = (sample_res(choice(["company_postfix_casual", "genericplace"]))["id"][0]).title()
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


def company_name_suffix(biztype: str):
    suffixes = []
    used_already = []
    # TODO: Identify and add some other suffixes
    for i in range(randint(1, 2)):
        this_choice = choice(["company_postfix_formal"])
        if this_choice not in used_already:
            suffixes.append(sample_res(this_choice)["id"][0])
        used_already.append(this_choice)
    if biztype != "":
        if randint(0,3) == 0:
            suffixes.append(biztype)
    return suffixes
