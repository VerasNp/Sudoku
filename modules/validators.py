import re

from modules.json import get_json_key_content


def validate_input(data: any, message: dict, hint=False):
    if hint:
        for i in range(len(data)):
            if hint:
                if re.match(r"^[A-I],[1-9]:[1-9]$", data[i]):
                    continue
                else:
                    set_error_message(message, data[i])
        return
    else:
        if re.match(r"^[A-Ia-i]\s*,\s*[1-9]\s*:\s*[1-9]$", data) or re.match(r"^D[A-Ia-i],[1-9]$", data):
            return
        else:
            set_error_message(message, data)


def set_error_message(message: dict, data):
    if message["data"]:
        raise Exception(get_json_key_content(message["message"], message["key"]) % data)
    else:
        raise Exception(get_json_key_content(message["message"], message["key"]))


def validate_play(matrix, column, line, number, hint=False):
    if not hint:
        validate_play_is_hint(matrix, column, line)
    validate_area(matrix, number)
    validate_line(matrix, line, number)
    validate_column(matrix, column, number)


def validate_play_is_hint(matrix, column, line):
    for i in range(len(matrix)):
        for j in range(i):
            if matrix[line][column]["hint"]:
                raise Exception("Hint")


def validate_area(matrix, number):
    for i in range(len(matrix)):
        for j in range(i):
            if i >= 0 or i <= 2:
                if (j >= 0 or j <= 2) and (number == matrix[i][j]["number"]):
                    raise Exception(f"nop")
                elif (j >= 3 or j <= 5) and (number == matrix[i][j]["number"]):
                    raise Exception(f"nop")
                elif (j >= 6 or j <= 5) and (number == matrix[i][j]["number"]):
                    raise Exception(f"nop")
            elif i >= 3 or i <= 5:
                if (j >= 0 or j <= 2) and (number == matrix[i][j]["number"]):
                    raise Exception(f"nop")
                elif (j >= 3 or j <= 5) and (number == matrix[i][j]["number"]):
                    raise Exception(f"nop")
                elif (j >= 6 or j <= 5) and (number == matrix[i][j]["number"]):
                    raise Exception(f"nop")
            elif i >= 6 or i <= 8:
                if (j >= 0 or j <= 2) and (number == matrix[i][j]["number"]):
                    raise Exception(f"nop")
                elif (j >= 3 or j <= 5) and (number == matrix[i][j]["number"]):
                    raise Exception(f"nop")
                elif (j >= 6 or j <= 5) and (number == matrix[i][j]["number"]):
                    raise Exception(f"nop")


def validate_line(matrix, line, number):
    for i in range(len(matrix)):
        for j in range(i):
            if i == line and number == matrix[i][j]["number"]:
                raise Exception(f"nop")


def validate_column(matrix, column, number):
    for i in range(len(matrix)):
        for j in range(i):
            if j == column and number == matrix[i][j]["number"]:
                raise Exception(f"nop")


def validate_hints_qtd(data):
    if len(data) < 1:
        raise Exception(get_json_key_content("resources.messages.err.pt_br", "HINT_QTD_MIN"))
    elif len(data) > 80:
        raise Exception(get_json_key_content("resources.messages.err.pt_br", "HINT_QTD_MAX"))
