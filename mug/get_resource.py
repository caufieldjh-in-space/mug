"""Utilities to get text from resources."""

from distutils.command.clean import clean
import heapq
from pathlib import Path
import random

RES_DIR = "resources"
ITEM_TYPES = {"beverage": "beverages.tsv",
              "color": "colors.tsv",
              "flavor": "flavors.tsv",
              "food": "foods.tsv",
              "food producer": "food_producers.tsv",
              "furniture": "furniture.tsv",
              "home electronic": "home_electronics.tsv",
              "image": "images.tsv",
              "mood": "moods.tsv",
              "zip code": "zip_codes.tsv"
             }

def get_items(item_type: str,
              count: int = 1,
              ) -> list:

    mod_path = Path(__file__).parent
    res_file = (mod_path / RES_DIR / ITEM_TYPES[item_type]).resolve()

    with res_file.open() as infile:
        header = (infile.readline().rstrip()).split("\t")
        sample = heapq.nlargest(count, 
                                infile,
                                key=lambda L: random.random()
                                )

    sample = _prep_sample(sample, header)

    return sample

def _prep_sample(rawlist: list, header: list = []) -> list:

    prepped_sample = []

    cleanlist = [s.strip() for s in rawlist]
    
    for value_set in cleanlist:
        values = value_set.split("\t")
        kvs = dict(zip(header,values))
        prepped_sample.append(kvs)

    return prepped_sample