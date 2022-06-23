from modules.file import get_json_path
from modules.json import read_json_file
from modules.string import string_navigation


def get_message_json(data):
    arr_path = string_navigation(data)
    key = arr_path[len(arr_path) - 1]
    path = get_json_path(arr_path)
    data_json = read_json_file(path)
    if key not in data_json:
        raise Exception("Chave não existe!")
    else:
        return data_json[key]
