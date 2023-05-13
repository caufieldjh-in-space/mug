"""textgen.py - general text generation tools"""

import random
import string

VOWELS = "aeiouAEIOU"

def make_acronym() -> str:
    """Make an acronym."""

    text = ""
    for _ in range(0, random.randint(3, 6)):
        text = text + random.choice(string.ascii_uppercase)
    
    return text