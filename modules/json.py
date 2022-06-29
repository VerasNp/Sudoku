import json

from modules.file import file_exists, get_base_dir, path_constructor


def get_json_file_content(path: str) -> dict:
    """
    Gets content from json file
    :param path:
    :return:
    """
    full_path = get_base_dir(True) + path
    file_exists(full_path, "json")
    path = path_constructor(full_path, "json")

    with open(path) as json_data:
        path = json_data.read()
        content = json.loads(path)

    return content


def get_json_key_content(path: str, key: str) -> str:
    """
    Get json key content
    :param path:
    :param key:
    :return:
    """
    content = get_json_file_content(path)

    if key not in content:
        raise Exception(f"{key} not exists!")
    else:
        return content[key]
