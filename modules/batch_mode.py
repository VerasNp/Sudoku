import copy

from modules.file import read_file
from modules.matrix import insert_input_sudoku, init_matrix_hints, check_full
from modules.render import render_sudoku


def start_batch_mode(init_matrix, data):
	"""
	Batch mode
	:param init_matrix:
	:param data:
	:return:
	"""
	initiated = init_matrix_hints(
		matrix=init_matrix,
		data=data,
		batch=True
	)

	render_sudoku(initiated)

	check_full(initiated)

	aux = copy.deepcopy(initiated)

	plays = read_file(data[1])

	matrix = insert_input_sudoku(aux, plays, False, True)

	check_matrix(initiated, matrix)


def check_matrix(old, new):
	"""
	Checks if the matrix was filled based on its state (old and new)
	:param old:
	:param new:
	:return:
	"""
	if new is None:
		exit("A grade nao foi preenchida!")
	else:
		i = 0
		while i < len(new):
			j = 0
			while j < len(new[i]):
				if new[i][j]["number"] != old[i][j]["number"]:
					exit("A grade foi preenchida com sucesso!")
				j += 1
			i += 1
		# for i in range(len(new)):
		# 	for j in range(i):
		# 		if new[i][j]["number"] != old[i][j]["number"]:

