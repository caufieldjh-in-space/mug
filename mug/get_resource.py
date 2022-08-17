"""Utilities to get text from resources."""

import heapq
import random
from pathlib import Path

RES_DIR = "resources"
# TODO: move these types out to their own file
# TODO: more resources!
RES_TYPES = { "address modifier": "address_modifiers.tsv",
              "animal": "animals.tsv",
              "beverage": "beverages.tsv",
              "beverage producer": "beverage_producers.tsv",
              "business type": "business_types.tsv",
              "clothes": "clothes.tsv",
              "color": "colors.tsv",
              "company postfix casual": "company_postfixes_casual.tsv",
              "company postfix formal": "company_postfixes_formal.tsv",
              "corporate department": "corporate_departments.tsv",
              "english word": "english_words.tsv",
              "fictional beast": "fictional_beasts.tsv",
              "fictional character": "fictional_characters.tsv",
              "flavor": "flavors.tsv",
              "food": "foods.tsv",
              "forename": "forenames.tsv",
              "furniture": "furniture.tsv",
              "generic place": "generic_places.tsv",
              "home electronic": "home_electronics.tsv",
              "image": "images.tsv",
              "industry": "industries.tsv",
              "latin word": "latin_words.tsv",
              "mood": "moods.tsv",
              "postnominative title": "postnom_titles.tsv",
              "prenominative title": "prenom_titles.tsv",
              "slogan": "slogans.tsv",
              "street postfix": "street_postfixes.tsv",
              "surname": "surnames.tsv",
              "technology": "technologies.tsv",
              "us states": "us_states.tsv",
              "world cities": "world_cities.tsv",
              "world countries": "world_countries.tsv",
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

def get_all_ids(res_type: str,
                ) -> list:

    mod_path = Path(__file__).parent
    res_file = (mod_path / RES_DIR / RES_TYPES[res_type]).resolve()

    ids = []

    with res_file.open() as infile:
        infile.readline() # Skip header
        for line in infile:
            ids.append((line.rstrip().split("\t"))[0])

    return ids

def _prep_sample(rawlist: list, header: list = []) -> list:

    prepped_sample = []

    cleanlist = [s.strip() for s in rawlist]
    
    for value_set in cleanlist:
        values = value_set.split("\t")
        kvs = dict(zip(header,values))
        prepped_sample.append(kvs)

    return prepped_sample
