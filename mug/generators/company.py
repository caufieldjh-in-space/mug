"""company.py - generate company names + metadata"""

import random
import string

from mug.generators.generic import MUGProduct
from mug.get_resource import get_items
from mug.utils.vary_text import all_upper, controlled_misspell, uncontrolled_misspell


class Company(MUGProduct):
    """Generate a company.

    By default, this only includes the name.
    Methods may be called to generate
    additional metadata; they are initialized
    as None.
    """

    def __init__(self):
        """Init - generate a name"""
        super().__init__()
        self.name = self.make_company_name()
        self.address = None
        self.industry = None
        self.slogan = None
        self.logo_description = None

    def make_company_name(self) -> str:

        #TODO: add portmanteu generator

        part_types = ["animal",
                      "color",
                      "fictional beast",
                      "fictional character",
                      "forename",
                      "generic place",
                      "mood",
                      "surname",
                      "us states",
                      "world cities",
                      "world countries"
                      ]

        tc = random.randint(0,2)
        if tc == 0: # Acronym
            name = ""
            for _ in range(0,random.randint(3,6)):
                name = name + random.choice(string.ascii_uppercase)
        elif tc == 1: # Simple word or phrase
            part1 = get_items(random.choice(part_types), 1)[0]["id"].title()
            if random.randint(0,4) == 0:
                name = f"{part1}"
            else:
                part2 = get_items(random.choice(part_types), 1)[0]["id"].title()
                name = f"{part1} {part2}"
        elif tc == 2: # Person name(s)
            parts = get_items("surname", 2)
            part1 = parts[0]["id"].title()
            part2 = parts[1]["id"].title()
            conn = random.choice(["", "-", " & "," And "])
            if random.randint(0,5) > 0:
                if random.randint(0,1) == 0:
                    part3 = get_items("surname", 1)[0]["id"].title()
                    name = f"{part1}, {part2} & {part3}"
                else:
                    if random.randint(0,1) == 0:
                        name = f"{part1}, {part2} & {part2}"
                    else:
                        name = f"{part1}{part2}{part2}"
            else:
                if random.randint(0,1) == 0:
                    name = f"{part1}{conn}{part2}"
                else:
                    name = f"{part1}"

        if random.randint(0,8) == 0:
            name = name.replace(" ", "")

        if random.randint(0,6) == 0:
            name = controlled_misspell(name)

        if random.randint(0,6) == 0:
            name = uncontrolled_misspell(name)

        if random.randint(0,9) == 0:
            name = all_upper(name)

        if random.randint(0,6) == 0:
            postfix = get_items("company postfix casual", 1)[0]["id"]
            name = f"{name}{postfix}"

        #TODO: align this with the industry object property
        if random.randint(0,3) == 0:
            parttype = random.choice(["business type", "industry"])
            busindtype = get_items(parttype, 1)[0]["id"]
            name = f"{name} {busindtype}"

        if random.randint(0,2) == 0:
            postfix = get_items("company postfix formal", 1)[0]["id"]
            name = f"{name} {postfix}"

        return name
