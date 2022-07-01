from modules.json import get_json_file_content


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
