"""company.py - generate company names + metadata"""

import random
import string

from mug.generators.generic import MUGProduct
from mug.get_resource import get_items
from mug.utils.vary_text import all_upper, controlled_misspell, uncontrolled_misspell


class Company(MUGProduct):
    """Generate a company."""

    def __init__(self):
        """Init"""
        super().__init__()
        self.industry = self.make_industry_name()
        self.name = self.make_company_name()
        self.address = self.make_company_address()
        self.slogan = self.make_company_slogan()
        self.logo_description = self.make_company_logo_description()


    def make_industry_name(self) -> str:

        industry = get_items(random.choice(["business type", "industry"]), 1)[0]["id"]

        return industry


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
            if self.industry:
                busindtype = self.industry
            else:
                parttype = random.choice(["business type", "industry"])
                busindtype = get_items(parttype, 1)[0]["id"]
                self.industry = busindtype
            name = f"{name} {busindtype}"

        if random.randint(0,2) == 0:
            postfix = get_items("company postfix formal", 1)[0]["id"]
            name = f"{name} {postfix}"

        return name


    def make_company_address(self) -> str:

        # TODO: see wastegenerator/waste_text_generators.py for address generator

        address = ""

        return address


    def make_company_slogan(self) -> str:

        nounchoice = random.choice([self.name,
                                    self.industry])
        if isinstance(nounchoice, str):
            noun = nounchoice

        slogbase = get_items("slogan", 1)[0]["id"]

        slogan = f"{slogbase} {noun}"

        for term in ["Service","Store"]:
            if slogan.endswith(term):
                slogan = " ".join((slogan.split())[:-1])

        return slogan


    def make_company_logo_description(self) -> str:

        logobase = get_items("image", 1)[0]["id"]

        if random.randint(0,1) == 0:
            descriptor_choice = random.choice(["color", "mood"])
            descriptor = get_items(descriptor_choice, 1)[0]["id"]
            logo_description = f"A {descriptor} {logobase}"
        else:
            if random.randint(0,1) == 0:
                count = random.choice(["Two","Three","Four","Five","Six"])
                logo_description = f"{count} {logobase}s"
            else:
                logo_description = f"A {logobase}"

        return logo_description