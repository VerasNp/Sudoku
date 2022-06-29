import os.path
from typing import Union

from modules.string import string_navigation


def get_base_dir(point_separator: bool = False):
    """
    Get project base dir
    :param point_separator:
    :return:
    """
    path_script = os.getcwd().split(os.path.sep)
    path = path_script[::-1]

    for i in range(len(path)):
        if path[i] != "Sudoku":
            path_script.remove(path[i])
        else:
            break

    path = ""

    for i in range(len(path_script)):
        path += path_script[i] + os.path.sep

    if point_separator:
        path = path.replace(os.path.sep, ".")[:]

    return path


def file_exists(data: str, ext=None) -> True:
    """
    Validates if the file exists
    :param ext:
    :param data:
    :return:
    """
    path = path_constructor(data, ext)

    if not os.path.isfile(path):
        raise Exception(f"{path} not found!")

    return True


def file_exists_list(data: list):
    """
    Validates if list of files exists
    :param data:
    :return:
    """
    for i in range(len(data)):
        if not os.path.isfile(data[i]):
            raise Exception(f"{data[i]} not found!")


def path_constructor(data: str, ext=None) -> str:
    """
    Constructs a path based on string separated by points
    :param data:
    :param ext:
    :return:
    """
    path_arr = string_navigation(data)
    path = ""

    for i in range(len(path_arr)):
        path += path_arr[i] + os.path.sep

    path = path[:-1]

    if ext:
        path += "." + str(ext)

    return path


def read_file(file):
    content = []
    with open(file) as f:
        while True:
            line = f.readline()
            if not line:
                break
            elif line == '\n':
                continue
            else:
                content.append(line.rstrip())
    return content


def check_ext(data: Union[list, str], ext: str) -> bool:
    """
    Validates file extension
    :param data:
    :param ext:
    :return:
    """
    path = path_constructor(data, ext)
    if not os.path.splitext(path)[1] == ("." + ext):
        raise Exception(f"{data} with invalid extension!")
    return True


def check_ext_list(data: list, ext: str):
    for i in range(len(data)):
        if not os.path.splitext(data[i])[1] == ("." + ext):
            raise Exception(f"{data[i]} with invalid extension!!")
        return True
