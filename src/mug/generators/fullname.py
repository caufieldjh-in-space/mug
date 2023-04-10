"""fullname"""

import uuid

def generate():

    this_id = str(uuid.uuid4())
    contents = {"id":this_id}

    return contents