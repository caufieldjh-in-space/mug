"""Nickname"""
# Not in schema yet - supplements FullName

from random import randint, choice
import sys

from mug.load_data import sample_res, lookup_res
from mug.constants import CONSONANTS, VOWELS

GEN_NAME = "Nickname"
GEN_MOD = sys.modules[__name__]


def generate(big_names: list):
    """Return a list of strings, where each is a nickname.
    Takes a list of strings as input so nicknames *may*
    reflect these."""

    # TODO: need a lookup function to retrieve corresponding nicknames
    # TODO: the usernames are pretty wild. Tone that one down.

    select = choice(
        [
            "get_random_nickname",
            "get_random_word_name",
            "get_some_other_name",
            "diminutize",
            "get_known_nickname",
            "make_into_initials",
            "make_username",
        ]
    )
    gen_func = getattr(GEN_MOD, select)
    contents = gen_func(big_names)

    return contents


def get_random_nickname(names):
    return sample_res("nickname")["id"]


def get_random_word_name(names):
    res_choice = choice(["animal", "english_word"])
    return [name.capitalize() for name in sample_res(res_choice)["id"]]


def get_some_other_name(names):
    return sample_res("givenname")["id"]


def diminutize(names):
    nickname = ""
    i = 0
    for j in names[0]:
        i = i + 1
        if i > 3 and j in VOWELS:
            if randint(0, 1) == 0:
                nickname = nickname + j
            break
        else:
            nickname = nickname + j

    if randint(0, 9) == 0 and nickname[-1] not in VOWELS:
        nickname = nickname + "y"

    if names[0] == nickname:
        nickname = nickname[0:2] + nickname[0:2]

    return [nickname]


def get_known_nickname(names):
    # Need to do a bit of parsing to get a list
    raw = lookup_res("givenname", names[0])["nickname"]
    nickname = [choice(raw[0].split(","))]
    if names[0] == nickname:
        nickname = diminutize(names)
    return nickname


def make_into_initials(names):
    return [choice([names[0][0], names[0][0] + names[1][0]])]


def make_username(names):
    username = ""
    for i in range(randint(4, 11)):
        if i % 2 == 0:
            username += choice(CONSONANTS)
        else:
            username += choice(VOWELS)
    if randint(0, 1) == 0:
        username += str(randint(0, 999))
    return [username]
