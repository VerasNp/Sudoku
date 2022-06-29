import re

from modules.json import get_json_file_content
from modules.string import search_data
from modules.validators import validate_play, validate_play_is_hint


def init_matrix(cols, lines, init_value):
    return [[init_value] * cols for _ in range(lines)]


def insert_input_sudoku(matrix, data, hint=False):
    dictionary = get_json_file_content("resources.dictionary")

    if isinstance(data, list):
        for i in range(len(data)):
            column = int(dictionary["COL"][0][search_data(data[i], "COL")])
            line = int(dictionary["LIN"][0][search_data(data[i], "LIN")])
            number = (search_data(data[i], "NUMBER"))

            validate_play(matrix, column, line, number, True)

            if hint:
                matrix[int(line)][int(column)] = {"number": number, "hint": True}
            else:
                matrix[int(line)][int(column)] = {"number": number, "hint": False}
    elif isinstance(data, str):
        if re.match(r"^D[A-Ia-i],[1-9]$", data):
            column = int(dictionary["COL"][0][search_data(data, "COL", True)])
            line = int(dictionary["LIN"][0][search_data(data, "LIN", True)])
            validate_play_is_hint(matrix, column, line)
            delete_input(matrix, column, line)
            return matrix
        column = int(dictionary["COL"][0][search_data(data, "COL")])
        line = int(dictionary["LIN"][0][search_data(data, "LIN")])
        number = (search_data(data, "NUMBER"))
        validate_play(matrix, column, line, number, hint)

        if hint:
            matrix[int(line)][int(column)] = {"number": number, "hint": True}
        else:
            matrix[int(line)][int(column)] = {"number": number, "hint": False}
    return matrix


def delete_input(matrix, column, line):
    for i in range(len(matrix)):
        for j in range(i):
            matrix[line][column]["number"] = " "

