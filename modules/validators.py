import re
from modules.messenger import get_message_json


def validate_input(data: any, message: str = "", message_data=False):
    if isinstance(data, list):
        for i in range(len(data)):
            if re.match(r"^[A-I],\s*[1-9]:\s[1-9]$", data[i]):
                continue
            else:
                if message_data:
                    raise Exception(get_message_json(message) % (data[i]))
                else:
                    raise Exception(get_message_json(message))
    elif isinstance(data, str):
        if re.match(r"^[A-I],\s*[1-9]:\s[1-9]$", data):
            return
        else:
            if message_data:
                raise Exception(get_message_json(message) % (data))
            else:
                raise Exception(get_message_json(message))
