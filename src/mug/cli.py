"""Command line interface for mug generators."""

import click
import uuid

from mug.load_class import load_model_class, load_generator_class

@click.command()
@click.argument("classname")
@click.option("--count", default=1, help="Number of items to generate in total.")
def main(classname: str, count: int):
    """CLI for MUG generators.
    :param classname: Name of class of object to generate.
    :param count: Number of items to generate in total.
    """

    model_class = load_model_class(classname)

    # Get the slot list for this
    example = model_class(id="NULL")
    slots = example.__dict__

    for _ in range(count):
        genclass = load_generator_class(classname)
        kwargs = genclass()
        new_item = model_class(**kwargs)
        print(new_item)


if __name__ == "__main__":
    main()
