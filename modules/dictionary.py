import re

from modules.json import get_json_file_content
from modules.sanitize import sanitize_string


def search_key_by_value(general_key, searched_value):
	dictionary = get_json_file_content("resources.dictionary")
	specif_dictionary = dictionary[general_key][0]
	for key, val in specif_dictionary.items():
		if val == str(searched_value):
			return key


def search_value_by_key(general_key, searched_key):
	dictionary = get_json_file_content("resources.dictionary")
	specif_dictionary = dictionary[general_key][0]
	for key, val in specif_dictionary.items():
		if key == str(searched_key):
			return int(val)


def search_data(
	data_srch: str,
	search: str,
	is_delete=False):
	if search == 'COL':
		if is_delete:
			return search_value_by_key(
				general_key="COL",
				searched_key=sanitize_string(
					data=re.search(r"[A-Ia-i](?=\s*,)", data_srch).group(0).upper(),
					mode="rmv_wtspc"))
		else:
			return search_value_by_key(
				general_key="COL",
				searched_key=sanitize_string(
					data=re.search("[A-Ia-i]", data_srch).group(0).upper(),
					mode="rmv_wtsoc"
				))
	elif search == 'LIN':
		if is_delete:
			return search_value_by_key(
				general_key="LIN",
				searched_key=sanitize_string(
					data=re.search(r"(\d)+$", data_srch).group(0),
					mode="rmv_wtspc"))
		else:
			return search_value_by_key(
				general_key="LIN",
				searched_key=sanitize_string(
					data=re.search(r"\b(\d)+\s*(?=:)", data_srch).group(0),
					mode="rmv_wtspc"))
	elif search == 'NUMBER':
		return sanitize_string(
			data=re.search(r"(\d)+$", data_srch).group(0),
			mode="rmv_wtspc")
	else:
		raise Exception("%s nao mapeado" % search)
