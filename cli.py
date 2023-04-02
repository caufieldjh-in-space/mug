"""Command line interface for mug generators."""

import click

from generators.load_class import load_class

@click.command()
@click.argument("classname")
@click.option("--count", default=1, help="Number of items to generate in total.")
def main(classname: str, count: int):
    """CLI for MUG generators.
    :param classname: Name of class of object to generate.
    :param count: Number of items to generate in total.
    """

    for _ in range(count):
        gen = load_class(classname)
        print(gen)


if __name__ == "__main__":
    main()
