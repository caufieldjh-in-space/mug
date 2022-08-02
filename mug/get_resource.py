"""Utilities to get text from resources."""

import heapq
import random
from pathlib import Path

RES_DIR = "resources"
# TODO: move these types out to their own file
RES_TYPES = { "animal": "animals.tsv",
              "beverage": "beverages.tsv",
              "clothes": "clothes.tsv",
              "color": "colors.tsv",
              "company postfix": "company_postfixes.tsv",
              "flavor": "flavors.tsv",
              "food": "foods.tsv",
              "food producer": "food_producers.tsv",
              "forename": "forenames.tsv",
              "furniture": "furniture.tsv",
              "generic place": "generic_places.tsv",
              "home electronic": "home_electronics.tsv",
              "image": "images.tsv",
              "mood": "moods.tsv",
              "surname": "surnames.tsv",
              "technology": "technologies.tsv",
              "zip code": "zip_codes.tsv"
             }

def get_items(res_type: str,
              count: int = 1,
              ) -> list:

    mod_path = Path(__file__).parent
    res_file = (mod_path / RES_DIR / RES_TYPES[res_type]).resolve()

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
