"""textgen.py - general text generation tools"""

import random
import string

from get_resource import get_items

VOWELS = "aeiouAEIOU"

def make_acronym() -> str:
    """Make an acronym."""

    text = ""
    for _ in range(0, random.randint(3, 6)):
        text = text + random.choice(string.ascii_uppercase)
    
    return text

def make_phrase(part_types: list, count: int) -> str:
    """Return one or more words."""

    parts = get_items(random.choice(part_types), count)

    textlist = []
    for i in range(0,count):
        textlist.append(parts[i]["id"])
    text = " ".join(textlist)

    return text