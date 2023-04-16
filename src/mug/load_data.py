"""Load data from TSVs in resources directory."""

import polars as pl

from pathlib import Path

RESOURCE_DIR = Path("src/mug/resources")


def load_res(resname: str):
    """Load TSV and return full data frame."""
    fn = f"{resname}.tsv"
    respath = RESOURCE_DIR / fn

    res = pl.read_csv(respath, rechunk=False, separator="\t")

    return res

def sample_res(resname: str):
    """Retrieve a sample from a resource, returning a dict."""

    res = load_res(resname)

    sample = (res.sample(n=1)).to_dict(as_series=False)

    return sample
