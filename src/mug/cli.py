"""Command line interface for mug generators."""

import click
import uuid

from mug.load_class import load_class

@click.command()
@click.argument("classname")
@click.option("--count", default=1, help="Number of items to generate in total.")
def main(classname: str, count: int):
    """CLI for MUG generators.
    :param classname: Name of class of object to generate.
    :param count: Number of items to generate in total.
    """

    gen = load_class(classname)

    # Get the slot list for this
    example = gen(id="NULL")
    print(example.__dict__)

    for _ in range(count):
        
        this_id = str(uuid.uuid4())
        new_item = gen(id=this_id)

        print(new_item)


if __name__ == "__main__":
    main()
