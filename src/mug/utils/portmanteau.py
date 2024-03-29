"""portmanteu.py - create fun portmanteaus"""

from random import choice

def make_portmanteau(input: tuple) -> str:
    """Produce a portmanteau.

    Given a tuple of two lists,
    find a portmanteu of an entry from
    the first list and from the
    second list.
    """

    result = None

    list1 = input[0]
    list2 = input[1]

    term1 = choice(list1).lower()
    i = 1
    j = 1
    while not result:
        if i >= len(list2): # No matches found
            if j >= len(list1): # No options left
                result = term1
            else:
                term1 = choice(list1).lower() # Get a new term
                j = j +1
        term2 = choice(list2).lower()
        i = i +1
        for overlap in range(5,1,-1):
            if term1[-overlap:] == term2[0:overlap]:
                result = term1[:-overlap] + term2
                break
    
    return result
