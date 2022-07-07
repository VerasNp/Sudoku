def sanitize_list(mode, data: list, strict=False):
	old = data[:]

	if strict:
		for i in range(len(data)):
			data[i] = data[i].replace(" ", "")

	if mode == "rmv_dup":
		new_data = [""] * len(data)
		for i in range(len(data)):
			if not data[i] in new_data:
				new_data[i] = data[i]
		for i in range(len(new_data)):
			if new_data[i] != "":
				new_data[i] = old[i]
		data = list(filter(None, new_data))

	return data
