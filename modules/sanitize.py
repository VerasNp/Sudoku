def sanitize_list(mode: str, data: list):
	old = data[:]

	if mode == "rmv_dup":
		new_data = [""] * len(data)

		for i in range(len(data)):
			data[i] = sanitize_string("rmv_wtspc", data[i])

		for i in range(len(data)):
			if not data[i] in new_data:
				new_data[i] = data[i]
		for i in range(len(new_data)):
			if new_data[i] != "":
				new_data[i] = old[i]
		data = list(filter(None, new_data))
	elif mode == "rmv_empty":
		data = list(filter(None, data))
	return data


def sanitize_string(mode: str, data: str):
	if mode == "rmv_wtspc":
		data = data.replace(" ", "")
	return data
