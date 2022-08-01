"""company.py - generate company names + metadata"""

from mug.get_resource import get_items
from mug.generators.generic import MUGProduct

class Company(MUGProduct):
    """ Generate a company. 
    
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
        name = ""

        mood = get_items('mood',1)[0]['id'].title()
        animal = get_items('animal',1)[0]['id'].title().replace(" ", "")
        name = f"{mood}{animal}"

        return name