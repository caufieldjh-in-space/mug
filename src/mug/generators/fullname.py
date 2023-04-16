"""FullName"""

import uuid

from mug.load_class import get_class_details

GEN_NAME = "FullName"

def generate():

    details = get_class_details(GEN_NAME)
    print(details)

    this_id = str(uuid.uuid4())
    contents = {"id":this_id}

    return contents