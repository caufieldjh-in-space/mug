"""Utilities to get text from resources."""

from distutils.command.clean import clean
import heapq
from pathlib import Path
import random

RES_DIR = "resources"
ITEM_TYPES = {"color": "colors.tsv",
              "zip code": "zip_codes.tsv"
             }

def get_items(item_type: str,
              count: int = 1,
              ) -> list:

    mod_path = Path(__file__).parent
    res_file = (mod_path / RES_DIR / ITEM_TYPES[item_type]).resolve()

    with res_file.open() as infile:
        sample = heapq.nlargest(count, 
                                infile,
                                key=lambda L: random.random()
                                )

    sample = clean_sample(sample)

    return sample

def clean_sample(rawlist: list) -> list:

    cleanlist = [s.strip() for s in rawlist]

    return cleanlist