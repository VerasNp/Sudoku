from modules.matrix import insert_input_sudoku, init_matrix_hints, check_full
from modules.render import render_sudoku
from modules.terminal import cls
from modules.validators import validate_input


def start_interactive_mode(init_matrix, data):
    initiated = init_matrix_hints(init_matrix, data)

    check_full(initiated)

    render_sudoku(initiated)

    while True:
        try:
            entry = input("Entre com a sua jogada: ")
            validate_input(entry, {"message": "resources.messages.err.pt_br", "key": "INPUT", "data": True})
            aux = insert_input_sudoku(initiated, entry, False, False)[:]
            render_sudoku(aux)
            check_full(aux)
        except KeyboardInterrupt:
            cls()
            exit("Tchau :)")
        except EOFError:
            cls()
            exit("Tchau :)")
        except Exception as e:
            print(e)
