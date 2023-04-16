"""Load data from TSVs in resources directory."""

import polars as pl
import pandas as pd

from pathlib import Path

RESOURCE_DIR = Path("src/mug/resources")


def load_res(resname: str):
    """Load TSV and return data frame."""
    fn = f"{resname}.tsv"
    respath = RESOURCE_DIR / fn

    res = pl.read_csv(respath, rechunk=False, separator="\t").to_pandas()

    return res
