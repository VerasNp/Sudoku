import json


def read_json_file(path) -> dict:
    with open(path) as json_data:
        data = json_data.read()
        messages = json.loads(data)
    return messages
