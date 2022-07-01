import re

from modules.file import read_file
from modules.json import get_json_file_content
from modules.string import search_data
from modules.validators import validate_play, validate_play_is_hint, validate_inputs_qtd, validate_input


def init_matrix(cols, lines, init_value):
	return [[init_value] * cols for _ in range(lines)]


def insert_input_sudoku(matrix, data, hint=False, batch=False):
	dictionary = get_json_file_content("resources.dictionary")
	if isinstance(data, list):
		for i in range(len(data)):
			column = int(dictionary["COL"][0][search_data(data[i], "COL").upper()])
			line = int(dictionary["LIN"][0][search_data(data[i], "LIN")])
			number = (search_data(data[i], "NUMBER"))
			if validate_play(matrix, column, line, number, hint, batch):
				matrix[int(line)][int(column)] = {"number": number, "hint": hint}
			else:
				pass

	elif isinstance(data, str):
		if re.match(r"^D[A-Ia-i],[1-9]$", data):
			column = int(dictionary["COL"][0][search_data(data, "COL", True).upper()])
			line = int(dictionary["LIN"][0][search_data(data, "LIN", True)])
			validate_play_is_hint(matrix, column, line, False)
			delete_input(matrix, column, line)
			return matrix

		column = int(dictionary["COL"][0][search_data(data, "COL").upper()])
		line = int(dictionary["LIN"][0][search_data(data, "LIN")])
		number = (search_data(data, "NUMBER"))

		if validate_play(matrix, column, line, number, hint, batch):
			matrix[int(line)][int(column)] = {"number": number, "hint": hint}
		else:
			return
	return matrix


def delete_input(matrix, column, line):
	for i in range(len(matrix)):
		for j in range(i):
			matrix[line][column]["number"] = " "


def init_matrix_hints(matrix, data):
	hints = read_file(data[0])

	validate_inputs_qtd(hints)

	validate_input(hints, {"message": "resources.messages.err.pt_br", "key": "INPUT", "data": True}, True)

	return insert_input_sudoku(matrix, hints, True, False)


def check_full(matrix):
	for i in range(len(matrix)):
		for j in range(i):
			if " " in matrix[i][j]["number"]:
				return
	exit("Parabens! Você completou o Sudoku!")
