import re

from modules.dictionary import search_key_by_value
from modules.json import get_json_key_content
from modules.sanitize import sanitize_string
from modules.utils import dd


def set_error_message(
	err_message: dict,
	data: any = None,
	batch_mode: bool = False):
	if data is not None:
		if batch_mode:
			print(get_json_key_content(err_message["message"], err_message["key"]) % data)
		else:
			raise Exception(get_json_key_content(err_message["message"], err_message["key"]) % data)
	else:
		if batch_mode:
			print(get_json_key_content(err_message["message"], err_message["key"]) % data)
		else:
			raise Exception(get_json_key_content(err_message["message"], err_message["key"]))


def validate_input_format(
	data: any,
	message: dict,
	hint: bool = False,
	batch_mode: bool = False):
	if isinstance(data, list):
		for i in range(len(data)):
			if hint:
				if not re.match(r"[A-I],[1-9]:[1-9]$", data[i]):
					exit(get_json_key_content(message["path"], message["key"]))
			else:
				if not (
					re.match(r"\s*[A-Ia-i]\s*,\s*[1-9]\s*:\s*[1-9]$", data[i])
					or re.match(r"\s*D[A-Ia-i]\s*,\s*[1-9]$", data[i])):
					set_error_message(
						err_message={
							"message": "resources.messages.err.pt_br",
							"key": "GENERIC_INPUT",
							"data": True},
						data=data[i],
						batch_mode=batch_mode)
	else:
		if hint:
			if not re.match(r"[A-I],[1-9]:[1-9]$", data):
				exit(get_json_key_content(message["path"], message["key"]))
		else:
			if not (re.match(r"\s*[A-Ia-i]\s*,\s*[1-9]\s*:\s*[1-9]$", data) or re.match(r"\s*D[A-Ia-i]\s*,\s*[1-9]$",
																						data)):
				set_error_message(
					err_message={"message": "resources.messages.err.pt_br", "key": "GENERIC_INPUT", "data": True},
					data=sanitize_string(data=data, mode="rmv_wtspc"),
					batch_mode=batch_mode)
				return False
		return True


def validate_play(
	matrix: list,
	column: int,
	line: int,
	number: int,
	hint: bool = False,
	batch_mode: bool = False):
	play_not_override_hint = True

	if not hint:
		play_not_override_hint = validate_play_override_hint(matrix, column, line, number, batch_mode)

	if (
		play_not_override_hint and
		validate_area(matrix, column, line, number, hint, batch_mode) and
		validate_line(matrix, column, line, number, hint, batch_mode) and
		validate_column(matrix, column, line, number, hint, batch_mode)
	):
		return True
	else:
		return False


def validate_play_override_hint(
	matrix: list,
	column: int,
	line: int,
	number: int = None,
	batch_mode: bool = False,
	is_delete: bool = False):
	if matrix[line][column]["hint"]:
		column = search_key_by_value("COL", column)
		line = search_key_by_value("LIN", line)

		if batch_mode:
			if is_delete:
				set_error_message(
					err_message={"message": "resources.messages.err.pt_br", "key": "DELETE_INPUT", "data": True},
					data=(column, line),
					batch_mode=True)
			else:
				set_error_message(
					err_message={"message": "resources.messages.err.pt_br", "key": "INPUT", "data": True},
					data=(column, line, number),
					batch_mode=True)
		else:
			set_error_message(
				err_message={"message": "resources.messages.err.pt_br", "key": "DATA_HINT", "data": True},
				data=(column, line),
				batch_mode=False)
		return False
	return True


def validate_area(
	matrix: list,
	column: int,
	line: int,
	number: int,
	hint: bool = False,
	batch_mode: bool = False):
	val = True
	if (
		column == 0 or
		column == 1 or
		column == 2):
		if line == 0 or line == 1 or line == 2:
			val = check_area(
				matrix=matrix, number=number, batch_mode=batch_mode, start_line=0, end_line=2, start_column=0,
				end_column=2, hint=hint)
		elif line == 3 or line == 4 or line == 5:
			val = check_area(
				matrix=matrix, number=number, batch_mode=batch_mode, start_line=3, end_line=5, start_column=0,
				end_column=2, hint=hint)
		elif line == 6 or line == 7 or line == 8:
			val = check_area(
				matrix=matrix, number=number, batch_mode=batch_mode, start_line=6, end_line=8, start_column=0,
				end_column=2, hint=hint)
	elif (
		column == 3 or
		column == 4 or
		column == 5):
		if line == 0 or line == 1 or line == 2:
			val = check_area(
				matrix=matrix, number=number, batch_mode=batch_mode, start_line=0, end_line=2, start_column=3,
				end_column=5, hint=hint)
		elif line == 3 or line == 4 or line == 5:
			val = check_area(
				matrix=matrix, number=number, batch_mode=batch_mode, start_line=3, end_line=5, start_column=3,
				end_column=5, hint=hint)
		elif line == 6 or line == 5 or line == 8:
			val = check_area(
				matrix=matrix, number=number, batch_mode=batch_mode, start_line=6, end_line=8, start_column=3,
				end_column=5, hint=hint)
	elif (
		column == 6 or
		column == 7 or
		column == 8):
		if line == 0 or line == 1 or line == 2:
			val = check_area(
				matrix=matrix, number=number, batch_mode=batch_mode, start_line=0, end_line=2, start_column=6,
				end_column=8, hint=hint)
		elif line == 3 or line == 4 or line == 5:
			val = check_area(
				matrix=matrix, number=number, batch_mode=batch_mode, start_line=3, end_line=5, start_column=6,
				end_column=8, hint=hint)
		elif line == 6 or line == 7 or line == 8:
			val = check_area(
				matrix=matrix, number=number, batch_mode=batch_mode, start_line=6, end_line=8, start_column=6,
				end_column=8, hint=hint)
	return val


def check_area(
	matrix: list,
	number: int,
	start_line: int,
	end_line: int,
	start_column: int,
	end_column: int,
	hint: bool = False,
	batch_mode: bool = False):
	i = start_line
	while i <= end_line:
		j = start_column
		while j <= end_column:
			if matrix[i][j]["number"] == number:
				if hint:
					exit(get_json_key_content("resources.messages.err.pt_br", "HINT_CONFIG"))
				else:
					column = search_key_by_value("COL", j)
					line = search_key_by_value("LIN", i)
					if batch_mode:
						set_error_message(
							err_message={"message": "resources.messages.err.pt_br", "key": "INPUT", "data": True},
							data=(column, line, number),
							batch_mode=True)
					else:
						set_error_message(
							err_message={"message": "resources.messages.err.pt_br", "key": "DATA_AREA", "data": True},
							data=(number, column, line),
							batch_mode=False)
					return False
			j += 1
		i += 1
	return True


def validate_line(
	matrix: list,
	column: int,
	line: int,
	number: int,
	hint: bool = False,
	batch_mode: bool = False):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if i == line and number == matrix[i][j]["number"]:
				if hint:
					exit(get_json_key_content("resources.messages.err.pt_br", "HINT_CONFIG"))
				else:
					column = search_key_by_value("COL", column)
					line = search_key_by_value("LIN", line)
					if batch_mode:
						set_error_message(
							err_message={"message": "resources.messages.err.pt_br", "key": "INPUT", "data": True},
							data=(column, line, number),
							batch_mode=True)
					else:
						set_error_message(
							err_message={"message": "resources.messages.err.pt_br", "key": "DATA_LINE", "data": True},
							data=(number, line),
							batch_mode=False)
					return False
	return True


def validate_column(
	matrix: list,
	column: int,
	line: int,
	number: int,
	hint: bool = False,
	batch_mode: bool = False):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if j == column and number == matrix[i][j]["number"]:
				if hint:
					exit(get_json_key_content("resources.messages.err.pt_br", "HINT_CONFIG"))
				else:
					column = search_key_by_value("COL", column)
					line = search_key_by_value("LIN", line)
					if batch_mode:
						set_error_message(
							err_message={"message": "resources.messages.err.pt_br", "key": "INPUT", "data": True},
							data=(column, line, number),
							batch_mode=True)
					else:
						set_error_message(
							err_message={"message": "resources.messages.err.pt_br", "key": "DATA_COLUMN", "data": True},
							data=(number, column),
							batch_mode=False)
					return False
	return True


def validate_hints_qtd(hints: list) -> None:
	total = len(hints)

	if total < 1:
		raise Exception(get_json_key_content("resources.messages.err.pt_br", "HINT_QTD_MIN"))
	elif total == 80:
		return
	elif total > 80:
		raise Exception(get_json_key_content("resources.messages.err.pt_br", "HINT_QTD_MAX"))
