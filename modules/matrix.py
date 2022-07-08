import re

from modules.file import read_file
from modules.sanitize import sanitize_list
from modules.dictionary import search_data
from modules.utils import dd
from modules.validators import validate_play, validate_hints_qtd, validate_input_format, validate_play_override_hint


def init_sudoku_matrix():
	return [[{"number": " ", "hint": None}] * 9 for _ in range(9)]


def insert_input_sudoku(
	matrix: list,
	data: any,
	hint: bool = False,
	batch_mode: bool = False):
	if isinstance(data, list):
		for i in range(len(data)):
			if re.match(r"\s*D([A-Ia-i])+", data[i]):
				column = search_data(
					data_srch=data[i],
					search="COL",
					is_delete=True
				)
				line = search_data(
					data_srch=data[i],
					search="LIN",
					is_delete=True
				)
				if (validate_play_override_hint(
					matrix=matrix,
					column=column,
					line=line,
					batch_mode=batch_mode,
					is_delete=True
				)):
					delete_input(matrix, column, line)
				else:
					pass
			else:
				if validate_input_format(
					data[i], {"message": "resources.messages.err.pt_br", "key": "INPUT", "data": True}, hint,
					batch_mode):
					column = search_data(
						data_srch=data[i],
						search="COL"
					)
					line = search_data(
						data_srch=data[i],
						search="LIN"
					)
					number = search_data(
						data_srch=data[i],
						search="NUMBER"
					)

					if (validate_play(
						matrix=matrix,
						column=column,
						line=line,
						number=number,
						hint=hint,
						batch_mode=batch_mode
					)):
						matrix[line][column] = {"number": number, "hint": hint}
					else:
						pass
				else:
					pass
	else:
		if re.match(r"\s*D([A-Ia-i])+", data):
			column = search_data(
				data_srch=data,
				search="COL",
				is_delete=True
			)
			line = search_data(
				data_srch=data,
				search="LIN",
				is_delete=True
			)

			if (validate_play_override_hint(
				matrix=matrix,
				column=column,
				line=line,
				batch_mode=batch_mode,
				is_delete=True
			)):
				delete_input(matrix, column, line)
			else:
				pass
		else:
			if validate_input_format(
				data, {"message": "resources.messages.err.pt_br", "key": "INPUT", "data": True}, hint,
				batch_mode):
				column = search_data(
					data_srch=data,
					search="COL"
				)
				line = search_data(
					data_srch=data,
					search="LIN"
				)
				number = search_data(
					data_srch=data,
					search="NUMBER"
				)
				if (validate_play(
					matrix=matrix,
					column=column,
					line=line,
					number=number,
					hint=hint,
					batch_mode=batch_mode
				)):
					matrix[line][column] = {"number": number, "hint": hint}
				else:
					pass
			else:
				pass

	return matrix


def delete_input(matrix, column, line):
	for i in range(len(matrix)):
		for j in range(i):
			matrix[line][column]["number"] = " "


def init_matrix_hints(
	matrix: list,
	hint_file: str,
	batch: bool = False
):
	hints = read_file(file=hint_file)

	validate_hints_qtd(hints=hints)

	hints = sanitize_list(
		mode="rmv_dup",
		data=hints)

	validate_input_format(
		data=hints,
		message={"path": "resources.messages.err.pt_br", "key": "HINT_CONFIG"},
		hint=True,
		batch_mode=batch)

	return insert_input_sudoku(
		matrix=matrix,
		data=hints,
		hint=True,
		batch_mode=batch)


def check_full(matrix: list):
	i = 0
	while i < len(matrix):
		j = 0
		while j < len(matrix[i]):
			if " " == matrix[i][j]["number"]:
				return
			j += 1
		i += 1

	exit("Parabens! Você completou o Sudoku!")
