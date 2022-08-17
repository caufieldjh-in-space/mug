"""person.py - generate person names and details"""

from mug.generators.generic import MUGProduct
from mug.get_resource import get_items


class Person(MUGProduct):
    """Generate a company."""

    def __init__(self):
        """Init"""
        # TODO: make distinction between formal and informal name

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
        # TODO: expand based on wastegen namegen

        forename = get_items("forename", 1)[0]["id"]
        surname = get_items("surname", 1)[0]["id"]
        name = f"{forename} {surname}"

        return name
