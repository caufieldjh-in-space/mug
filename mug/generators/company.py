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

    def make_company_name(self) -> str:
        name = ""

        sample = get_items('mood',1)
        name = sample[0]['id']

        name = name.title()

        return name