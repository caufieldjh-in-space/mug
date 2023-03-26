"""person.py - generate person names and details"""

import random

from generic import MUGProduct
from get_resource import get_items, get_mapped_ids
from utils.textgen import VOWELS


class Person(MUGProduct):
    """Generate a person's metadata."""

    def __init__(self):
        """Init"""

        super().__init__()
        (self.name_informal, self.name_formal) = self.make_person_name()

    def make_person_name(self) -> tuple:
        """Produce two versions of a person's name.

        The result is a tuple. The first entry
        is the informal name, e.g.,
        Craigley Pitts
        and the second entry is the formal name, e.g.,
        Prof. Craigley Nortimer Pitts, Esq
        The level of detail present in the casual name
        is random - it may be as short as a single name,
        but will generally include a forename and surname
        without titles."""

        # TODO: increase frequency of *some* names
        #       just because a small subset are very common

        forename = get_items("forename", 1)[0]["id"]
        surname = get_items("surname", 1)[0]["id"]
        middlename = get_items(random.choice(["forename", "surname"]), 1)[0]["id"]

        if random.randint(0, 19) == 0:  # Hyphenate surname
            surname = surname + "-" + get_items("surname", 1)[0]["id"]

        if random.randint(0, 79) == 0:
            forename = ""
            middlename = ""

        formname = f"{forename} {middlename} {surname}".lstrip()

        if random.randint(0, 19) == 0:
            title = get_items("prenominative title", 1)[0][
                random.choice(["id", "full_title"])
            ]
            formname = f"{title} {formname}"

        if random.randint(0, 29) == 0:
            title = get_items("postnominative title", 1)[0]["id"]
            formname = f"{formname} {title}"

        if random.randint(0, 9) == 0 and len(middlename) > 0:
            middlename = middlename[0].upper() + "."
        else:
            middlename = ""
        if random.randint(0, 49) == 0 and len(forename) > 0:
            forename = forename[0].upper() + "."
        if random.randint(0, 49) == 0:
            forename = ""
            middlename = ""
        if random.randint(0, 19) == 0:
            forename = get_nickname(forename)

        infname = f"{forename} {middlename} {surname}".lstrip()

        # A bit of cleanup
        formname = " ".join(formname.split())
        infname = " ".join(infname.split())

        namepair = (infname, formname)

        return namepair


def get_nickname(name: str) -> str:
    """Retrieve a nickname for the provided name.

    This may be a known nickname provided by the
    forename resources,
    or may be generated by this function.
    """

    nickname = ""

    namechoice = random.randint(0, 9)

    if namechoice < 6:
        i = 0
        for j in name:
            i = i + 1
            if i > 3 and j in VOWELS:
                if random.randint(0, 1) == 0:
                    nickname = nickname + j
                break
            else:
                nickname = nickname + j

        if random.randint(0, 19) == 0 and nickname[-1] not in VOWELS:
            nickname = nickname + "y"
    elif 5 < namechoice < 9:  # Look up a nickname
        all_nicknames = get_mapped_ids("forename")
        one_name = (name.split())[0]
        try:
            nicknames = (all_nicknames[one_name]).split(",")
            nickname = random.choice(nicknames).strip()
        except KeyError:
            nickname = name
    elif namechoice == 9:
        nickname = (get_items("animal", 1)[0]["id"]).title()

    return nickname
