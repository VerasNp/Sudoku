import copy

from modules.file import read_file
from modules.matrix import insert_input_sudoku, init_matrix_hints, check_full


def start_batch_mode(init_matrix, data):
	initiated = init_matrix_hints(init_matrix, data)
	check_full(initiated)
	aux = copy.deepcopy(initiated)
	plays = read_file(data[1])
	matrix = insert_input_sudoku(aux, plays, False, True)
	check_matrix(initiated, matrix)


def check_matrix(old, new):
	if new is None:
		exit("A grade nao foi preenchida!")
	else:
		for i in range(len(new)):
			for j in range(i):
				if new[i][j]["number"] != old[i][j]["number"]:
					exit("A grade foi preenchida com sucesso!")
