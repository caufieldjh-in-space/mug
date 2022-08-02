"""company.py - generate company names + metadata"""

import random

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

        part_types = ["animal", "color", "mood"]

        part1 = get_items(random.choice(part_types), 1)[0]["id"].title()
        part2 = get_items(random.choice(part_types), 1)[0]["id"].title()
        name = f"{part1}{part2}"
        name = name.replace(" ", "")

        if random.randint(0,6) == 0:
            name = controlled_misspell(name)

        if random.randint(0,6) == 0:
            name = uncontrolled_misspell(name)

        if random.randint(0,9) == 0:
            name = all_upper(name)

        return name
