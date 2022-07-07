import re

from modules.utils import dd


def search_data(data, search, is_delete=False):
	if search == 'COL':
		if is_delete:
			return re.search(r"(?!D)[A-Ia-i]", data).group(0)
		else:
			return re.search("[A-Ia-i]", data).group(0)
	elif search == 'LIN':
		if is_delete:
			return re.search(r"[1-9]$", data).group(0)
		else:
			return re.search(r"\b[1-9]\s*(?=:)", data).group(0)
	elif search == 'NUMBER':
		return re.search(r"[1-9]$", data).group(0)
	else:
		raise Exception('%s not mapped' % search)


def string_navigation(string: str) -> list:
	"""
	Returns a list based on string separated by points
	:param string:
	:return:
	"""

	# TODO: Improve separator check!
	return string.split(".")


def sanitize_string(mode, string: str):
	if mode == "rmv_spc":
		string = string.replace(" ", "")
	return string
