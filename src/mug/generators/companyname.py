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

    # TODO: enable inheritance here from Company
    bizchoice = sample_res(choice(["businesstype", "industry"]))
    biztype = bizchoice["id"][0]
    bizterms = bizchoice["terms"]

    for slot in details:
        if slot == "id":
            contents[slot] = str(uuid.uuid4())
        elif slot == "company_name_main":
            contents[slot] = company_name_main(bizterms)
        elif slot == "company_name_suffix":
            contents[slot] = company_name_suffix(biztype)
        else:
            gen_func = getattr(GEN_MOD, slot)
            contents[slot] = gen_func()

    # Format for printing

    if contents["company_name_suffix"]:
        fsuffix = " ".join(contents["company_name_suffix"])

    # TODO: enable the main to be an acronym version of the full name
    if contents["company_name_main"]:
        fcompany_name_main = " ".join(contents["company_name_main"])
        contents["description"] = f"{fcompany_name_main} {fsuffix}"
        contents["name"] = contents["company_name_main"][0]

    return contents


# TODO: inherit industry from parent if present
# TODO: add some more Weirdness
# TODO: add Tech Names
def company_name_main(bizterms: list):
    tc = randint(0, 6)
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
    elif tc == 1:  # Single, informal Person names
        namechoice = sample_res("givenname")
        name = choice([namechoice["id"][0], choice(namechoice["nickname"])])
        if randint(0, 5) == 0:
            name = f"{name}'s"
    elif tc == 2:  # Combined Person names
        name1 = sample_res("familyname")["id"][0]
        name2 = sample_res("familyname")["id"][0]
        conn1 = choice(["", " ", ", "])
        name = f"{name1}{conn1}{name2}"
        if randint(0, 3) == 0:
            name3 = sample_res("familyname")["id"][0]
            conn2 = choice(["", "-", " & ", " + ", " And "])
            name = f"{name}{conn2}{name3}"
    elif tc == 3:  # Generic names
        name = sample_res("genericcompanyname")["id"][0]
    elif tc == 4:  # Place names
        name = sample_res(choice(["animal", "english_word", "familyname", "givenname", "worldcity"]))["id"][0]
        if randint(0, 1) == 0:
            place_name = sample_res("genericplace")["id"][0]
            name = [name.title(), place_name.title()]
        else:
            street_postfix = sample_res("street_postfix")["id"][0]
            name = [name.title(), street_postfix]
        name = " ".join(name)
    elif tc == 5:  # Portmanteaus alone
        wordlist = (load_res("english_word")["id"]).to_list()
        name = make_portmanteau((wordlist, wordlist)).title()
    elif tc == 6:  # Tech name
        # TODO: to be completed (use the casual postfixes, and control syllables)
        basename = (
            sample_res(choice(["animal", "english_word", "givenname"]))["id"][0]
        ).title()
        name = basename

    # Modifiers
    if randint(0, 3) == 0:  # Add associated term
        postfix = (choice(bizterms)).title()
        if postfix != '':
            conn = choice(["", " "])
            name = f"{name}{conn}{postfix}"
    if randint(0, 9) == 0:
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
    if biztype != "":
        if randint(0, 2) == 0:
            suffixes.append(biztype)
    # TODO: Identify and add some other suffixes
    for i in range(randint(1, 2)):
        this_choice = choice(["company_postfix_formal"])
        if this_choice not in used_already:
            suffixes.append(sample_res(this_choice)["id"][0])
        used_already.append(this_choice)

    return suffixes
