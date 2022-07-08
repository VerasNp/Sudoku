import copy

from modules.file import read_file
from modules.matrix import insert_input_sudoku, init_matrix_hints, check_full


def start_batch_mode(init_matrix: list, files: list):
	hint_file = files[0]
	play_file = files[1]

	initiated_matrix = init_matrix_hints(
		matrix=init_matrix,
		hint_file=hint_file,
		batch=True
	)

	old_matrix = copy.deepcopy(initiated_matrix)

	plays = read_file(play_file)

	new_matrix = insert_input_sudoku(
		matrix=initiated_matrix,
		data=plays,
		hint=False,
		batch_mode=True)

	check_full(new_matrix)

	check_matrix(old_matrix, new_matrix)


def check_matrix(old, new):
	if new is None:
		exit("A grade nao foi preenchida!")
	else:
		count = 0
		i = 0
		while i < len(new):
			j = 0
			while j < len(new[i]):
				if new[i][j]["number"] != old[i][j]["number"]:
					exit("A grade foi preenchida com sucesso!")
				else:
					count += 1
				j += 1
			i += 1
		if count == 81:
			exit("A grade nao foi preenchida!")
