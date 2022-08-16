"""person.py - generate person names and details"""

from mug.generators.generic import MUGProduct
from mug.get_resource import get_items


class Person(MUGProduct):
    """Generate a company."""

    def __init__(self):
        """Init"""
        # TODO: make distinction between formal and informal name

        super().__init__()
        self.name = self.make_person_name()

    def make_person_name(self) -> str:

        # TODO: expand based on wastegen namegen

        forename = get_items("forename", 1)[0]["id"]
        surname = get_items("surname", 1)[0]["id"]
        name = f"{forename} {surname}"

        return name
