"""vary_text.py - functions for creating variation in strings"""

import random
import re
import string

STRPAIRS = [("s","z"),
            ("ing","x"),
            ("ing","in")
            ]

def controlled_misspell(instring: str):
    letterpair = random.choice(STRPAIRS)
    count = random.randint(1,3)
    instring = instring.replace(letterpair[0],
                                letterpair[1],
                                count)
    return instring

def uncontrolled_misspell(instring: str):
    all_letters = re.split("[^a-zA-Z]*", instring)
    alphabet = list(string.ascii_lowercase)
    letterpair = (random.choice(all_letters),
                  random.choice(alphabet)
                  )
    count = random.randint(1,3)
    instring = instring.replace(letterpair[0],
                                letterpair[1],
                                count)
    return instring