import re

from modules.dictionary import search_key_by_value
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


def validate_play(matrix, column, line, number, hint=False, batch=False):
	validate_play_hint = True
	if not hint:
		validate_play_hint = validate_play_is_hint(matrix, column, line, batch)

	if (validate_play_hint and
					validate_area(matrix, column, line, number, batch) and
					validate_line(matrix, column, line, number, batch) and
					validate_column(matrix, column, line, number, batch)):
		return True
	else:
		return False


def validate_play_is_hint(matrix, column, line, batch):

	if matrix[line][column]["hint"]:
		col = search_key_by_value("COL", column)
		lin = search_key_by_value("LIN", line)
		if batch:
			set_error_message({"message": "resources.messages.err.pt_br", "key": "BATCH_INPUT", "data": True}, (col, lin),
												True)
			return False
		else:
			set_error_message({"message": "resources.messages.err.pt_br", "key": "HINT_DATA", "data": True}, (col, lin))
			return False
	return True


def validate_area(matrix, column, line, number, batch):
	val = True
	if column == 0 or column == 1 or column == 2:
		if line == 0 or line == 1 or line == 2:
			val = check_area(matrix, number, batch, column, line, 0, 2, 0, 2)
		elif line == 3 or line == 4 or line == 5:
			val = check_area(matrix, number, batch, column, line, 3, 5, 0, 2)
		elif line == 6 or line == 7 or line <= 8:
			val = check_area(matrix, number, batch, column, line, 6, 8, 0, 2)
	elif column == 3 or column == 4 or column == 5:
		if line == 0 or line == 1 or line == 2:
			val = check_area(matrix, number, batch, column, line, 0, 2, 3, 5)
		elif line == 3 or line == 4 or line == 5:
			val = check_area(matrix, number, batch, column, line, 3, 5, 3, 5)
		elif line == 6 or line == 5 or line == 8:
			val = check_area(matrix, number, batch, column, line, 6, 8, 3, 5)
	elif column == 6 or column == 7 or column == 8:
		if line == 0 or line == 1 or line == 2:
			val = check_area(matrix, number, batch, column, line, 0, 2, 6, 8)
		elif line == 3 or line == 4 or line == 5:
			val = check_area(matrix, number, batch, column, line, 3, 5, 6, 8)
		elif line == 6 or line == 7 or line == 8:
			val = check_area(matrix, number, batch, column, line, 6, 8, 6, 8)
	return val


def check_area(matrix, number, batch, column, line, start_line, end_line, start_column, end_column):
	for i in range(start_line, end_line):
		for j in range(start_column, end_column):
			if matrix[i][j]["number"] == number:
				if batch:
					col = search_key_by_value("COL", column)
					lin = search_key_by_value("LIN", line)
					set_error_message({"message": "resources.messages.err.pt_br", "key": "BATCH_INPUT", "data": True}, (col, lin),
														True)
					return False
				else:
					column = search_key_by_value("COL", j)
					line = search_key_by_value("LIN", i)
					set_error_message({"message": "resources.messages.err.pt_br", "key": "DATA_AREA", "data": True},
														(number, column, line))
					return False
			else:
				return True


def validate_line(matrix, column, line, number, batch):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if i == line and number == matrix[i][j]["number"]:
				col = search_key_by_value("COL", column)
				lin = search_key_by_value("LIN", line)
				if batch:
					set_error_message({"message": "resources.messages.err.pt_br", "key": "BATCH_INPUT", "data": True},
														(col, lin), True)
					return False
				else:
					set_error_message({"message": "resources.messages.err.pt_br", "key": "DATA_LINE", "data": True},
														(number, lin))
					return False
	return True


def validate_column(matrix, column, line, number, batch):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if j == column and number == matrix[i][j]["number"]:
				col = search_key_by_value("COL", column)
				lin = search_key_by_value("LIN", line)
				if batch:
					set_error_message({"message": "resources.messages.err.pt_br", "key": "BATCH_INPUT", "data": True},
														(col, lin), True)
					return False
				else:
					set_error_message({"message": "resources.messages.err.pt_br", "key": "DATA_COLUMN", "data": True},
														(number, col))
					return False
	return True


def validate_inputs_qtd(data):
	if len(data) < 1:
		raise Exception(get_json_key_content("resources.messages.err.pt_br", "HINT_QTD_MIN"))
	elif len(data) == 80:
		return
	elif len(data) > 80:
		raise Exception(get_json_key_content("resources.messages.err.pt_br", "HINT_QTD_MAX"))




def set_error_message(message: dict, data, batch=False):
	"""
	{"message": str, "key": str, "data", bool}
		:param batch:
		:param message:
		:param data:
		:return:
	"""
	if message["data"]:
		if batch:
			print(get_json_key_content(message["message"], message["key"]) % data)
		else:
			raise Exception(get_json_key_content(message["message"], message["key"]) % data)
	else:
		if batch:
			print(get_json_key_content(message["message"], message["key"]) % data)
		else:
			raise Exception(get_json_key_content(message["message"], message["key"]))
