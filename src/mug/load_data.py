"""Load data from TSVs in resources directory."""

import polars as pl

from pathlib import Path

RESOURCE_DIR = Path("src/mug/resources")


# TODO: implement comma-delimited list parsing
# this only really needs to go in load_res
# see something like https://stackoverflow.com/questions/32742976/how-to-read-a-column-of-csv-as-dtype-list-using-pandas
# and https://stackoverflow.com/questions/71119197/polar-converters-like-pandas
# and check existing generators to see what that may impact


def load_res(resname: str):
    """Load TSV and return full data frame.

    Comma-delimited strings are parsed as lists.
    """
    fn = f"{resname}.tsv"
    respath = RESOURCE_DIR / fn

    res = pl.read_csv(respath, rechunk=False, separator="\t")

    return res


def sample_res(resname: str):
    """Retrieve a sample from a resource, returning a dict."""

    res = load_res(resname)

    sample = (res.sample(n=1)).to_dict(as_series=False)

    return sample


def lookup_res(resname: str, idselect: str):
    """Retrieve a row from a resource, given a resname and an ID.

    Returns a dict.
    """

    res = load_res(resname)

    row = res.filter(pl.col("id") == idselect).to_dict(as_series=False)

    return row
