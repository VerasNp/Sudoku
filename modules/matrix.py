import re

from modules.file import read_file
from modules.json import get_json_file_content
from modules.list import sanitize_list
from modules.string import search_data, sanitize_string
from modules.validators import validate_play, validate_play_is_hint, validate_hints_qtd, validate_input_format


def init_matrix(cols, lines, init_value):
	return [[init_value] * cols for _ in range(lines)]


def insert_input_sudoku(matrix, data, hint=False, batch=False):
	dictionary = get_json_file_content("resources.dictionary")

	if isinstance(data, list):
		for i in range(len(data)):
			column = sanitize_string("rmv_spc", search_data(data[i], "COL").upper())
			line = sanitize_string("rmv_spc", search_data(data[i], "LIN"))
			number = int(sanitize_string("rmv_spc", search_data(data[i], "NUMBER")))

			dict_column = int(dictionary["COL"][0][column])
			dict_line = int(dictionary["LIN"][0][line])

			if validate_play(matrix, dict_column, dict_line, int(number), hint, batch):
				matrix[dict_line][dict_column] = {"number": number, "hint": hint}
			else:
				pass

	elif isinstance(data, str):
		if re.match(r"^D[A-Ia-i],[1-9]$", data):
			column = sanitize_string("rmv_spc", search_data(data, "COL", True).upper())
			line = sanitize_string("rmv_spc", search_data(data, "LIN", True))

			dict_column = int(dictionary["COL"][0][column])
			dict_line = int(dictionary["LIN"][0][line])
			validate_play_is_hint(matrix, dict_column, dict_line, False, batch)
			delete_input(matrix, dict_column, dict_line)
		else:
			column = sanitize_string("rmv_spc", search_data(data, "COL").upper())
			line = sanitize_string("rmv_spc", search_data(data, "LIN"))
			number = int(sanitize_string("rmv_spc", search_data(data, "NUMBER")))

			dict_column = int(dictionary["COL"][0][column])
			dict_line = int(dictionary["LIN"][0][line])

			if validate_play(matrix, dict_column, dict_line, number, hint, batch):
				matrix[dict_line][dict_column] = {"number": number, "hint": hint}
			else:
				return
	return matrix


def delete_input(matrix, column, line):
	for i in range(len(matrix)):
		for j in range(i):
			matrix[line][column]["number"] = " "


def init_matrix_hints(matrix, data, batch=False):
	"""
	Init matrix with hints
	:param batch:
	:param matrix:
	:param data:
	:return:
	"""
	hints = read_file(data[0])

	if batch:
		hints = sanitize_list(
			mode="rmv_dup",
			strict=True,
			data=hints)

	validate_hints_qtd(hints)

	validate_input_format(
		data=hints,
		message={"message": "resources.messages.err.pt_br", "key": "HINT_CONFIG"},
		hint=True)

	return insert_input_sudoku(matrix, hints, True, False)


def check_full(matrix):
	"""
	Checks if the matrix was filled up
	:param matrix:
	:return:
	"""
	i = 0
	while i < len(matrix):
		j = 0
		while j < len(matrix[i]):
			if " " == matrix[i][j]["number"]:
				return
			j += 1
		i += 1

	exit("Parabens! Você completou o Sudoku!")
