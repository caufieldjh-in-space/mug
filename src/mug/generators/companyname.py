"""CompanyName"""

import sys
import uuid
from random import choice, randint

from mug.utils.textgen import make_acronym

from mug.load_class import get_class_details
from mug.load_data import sample_res

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


def company_name_main():
    tc = randint(0, 1)
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
                ]
            )
        )["id"][0].title()
    return [name]


def company_name_suffix():
    suffixes = []
    used_already = []
    for i in range(randint(1,2)):
        this_choice = choice(["company_postfix_formal", "corporate_department"])
        if this_choice not in used_already:
            suffixes.append(sample_res(this_choice)["id"][0])
        used_already.append(this_choice)
    return suffixes
