"""company.py - generate company names + metadata"""

import random

from mug.generators.address import Address
from mug.generators.person import Person
from mug.generators.generic import MUGProduct
from mug.get_resource import get_all_ids, get_items
from mug.utils.portmanteau import make_portmanteau
from mug.utils.textgen import make_acronym, make_phrase
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

        # TODO: add names based on location
        #       that will probably require passing the Address obj
        #       and include locations not present in the address as written
        # TODO: clean up random selection - separate functions would be nice

        part_types = [
            "animal",
            "english word",
            "fictional beast",
            "fictional character",
            "flavor",
            "forename",
            "generic place",
            "latin word",
            "mood",
            "surname",
            "us states",
            "world cities",
            "world countries",
        ]

        tc = random.randint(0, 5)
        if tc == 0:  # Acronym
            name = make_acronym()
        elif tc == 1:  # Simple word or phrase
            name = make_phrase(part_types, 1).title()
        elif tc == 2:
            name = make_phrase(part_types, random.randint(2,3)).title()
        elif tc == 3:  # Single person name
            # TODO: replace with full person name gen
            person = Person()
            name = person.name
        elif tc == 4:  # Multiple person names
            parts = get_items("surname", 2)
            part1 = parts[0]["id"].title()
            part2 = parts[1]["id"].title()
            conn = random.choice(["", "-", " & ", " And "])
            if random.randint(0, 5) > 0:
                if random.randint(0, 1) == 0:
                    part3 = get_items("surname", 1)[0]["id"].title()
                    name = f"{part1}, {part2} & {part3}"
                else:
                    if random.randint(0, 1) == 0:
                        name = f"{part1}, {part2} & {part2}"
                    else:
                        name = f"{part1}{part2}{part2}"
            else:
                if random.randint(0, 1) == 0:
                    name = f"{part1}{conn}{part2}"
                else:
                    name = f"{part1}"
        elif tc == 5:  # Portmanteau
            list1 = get_all_ids(random.choice(part_types))
            list2 = get_all_ids(random.choice(part_types))
            name = make_portmanteau((list1, list2)).title()

        if random.randint(0, 8) == 0:
            name = name.replace(" ", "")

        if random.randint(0, 6) == 0:
            name = controlled_misspell(name)

        if random.randint(0, 6) == 0:
            name = uncontrolled_misspell(name)

        if random.randint(0, 9) == 0:
            name = all_upper(name)

        if random.randint(0, 6) == 0:
            postfix = get_items("company postfix casual", 1)[0]["id"]
            name = f"{name}{postfix}"

        if random.randint(0, 3) == 0:
            if self.industry:
                if self.industry in [
                    "Beverages",
                    "Food And Beverage Consultant",
                    "Food And Beverage Exporter",
                    "Alcoholic Beverage Wholesaler",
                    "Beverage Distributor",
                ]:
                    busindtype = get_items("beverage producer", 1)[0]["id"]
                else:
                    busindtype = self.industry
                name = f"{name} {busindtype}"

        if random.randint(0, 2) == 0:
            postfix = get_items("company postfix formal", 1)[0]["id"]
            name = f"{name} {postfix}"

        return name

    def make_company_address(self) -> str:

        add_obj = Address()
        address = f"{add_obj.number} {add_obj.street}\n{add_obj.locality}"

        return address

    def make_company_slogan(self) -> str:

        # TODO: make more generative

        nounchoice = random.choice([self.name, self.industry])
        if isinstance(nounchoice, str):
            noun = nounchoice

        slogbase = get_items("slogan", 1)[0]["id"]

        slogan = f"{slogbase} {noun}"

        for term in ["Service", "Store"]:
            if slogan.endswith(term):
                slogan = " ".join((slogan.split())[:-1])

        return slogan

    def make_company_logo_description(self) -> str:

        # TODO: make more generative

        logobase = get_items("image", 1)[0]["id"]

        if random.randint(0, 1) == 0:
            descriptor_choice = random.choice(["color", "mood"])
            descriptor = get_items(descriptor_choice, 1)[0]["id"]
            logo_description = f"A {descriptor} {logobase}"
        else:
            if random.randint(0, 1) == 0:
                count = random.choice(["Two", "Three", "Four", "Five", "Six"])
                logo_description = f"{count} {logobase}s"
            else:
                logo_description = f"A {logobase}"

        return logo_description
