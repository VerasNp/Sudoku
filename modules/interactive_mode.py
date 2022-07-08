from modules.matrix import insert_input_sudoku, init_matrix_hints, check_full
from modules.render import render_sudoku
from modules.terminal import cls
from modules.validators import validate_input_format


def start_interactive_mode(init_matrix: list, files: list):
	hint_file = files[0]

	initiated_matrix = init_matrix_hints(
		matrix=init_matrix,
		hint_file=hint_file,
		batch=True
	)

	render_sudoku(initiated_matrix)

	print("""
		Bom jogo :)
		""")

	while True:
		try:
			entry = input("Entre com a sua jogada: ")

			validate_input_format(entry, {"message": "resources.messages.err.pt_br", "key": "INPUT", "data": True})

			new_matrix = insert_input_sudoku(initiated_matrix, entry, False, False)[:]

			# cls()

			render_sudoku(new_matrix)

			check_full(new_matrix)
		except KeyboardInterrupt:
			cls()
			exit("Tchau :)")
		except EOFError:
			cls()
			exit("Tchau :)")
		except Exception as e:
			print(e)
