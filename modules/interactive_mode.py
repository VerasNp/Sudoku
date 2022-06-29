from modules.file import read_file
from modules.matrix import insert_input_sudoku
from modules.render import render_sudoku
from modules.terminal import cls
from modules.validators import validate_hints_qtd, validate_input


def start_interactive_mode(init_matrix, data):
    initiated = init_matrix_hints(init_matrix, data)

    render_sudoku(initiated)

    while True:
        try:
            entry = input()
            validate_input(entry, {"message": "resources.messages.err.pt_br", "key": "INPUT", "data": True})
            aux = insert_input_sudoku(initiated, entry)[:]
            render_sudoku(aux)
            check_finished(aux)
        except KeyboardInterrupt:
            cls()
            exit("Tchau :)")
        except EOFError:
            cls()
            exit("Tchau :)")
        except Exception as e:
            print(e)


def init_matrix_hints(matrix, data):
    hints = read_file(data[0])

    validate_hints_qtd(hints)

    validate_input(hints, {"message": "resources.messages.err.pt_br", "key": "INPUT", "data": True}, True)

    return insert_input_sudoku(matrix, hints, True)


def check_finished(matrix):
    for i in range(len(matrix)):
        for j in range(i):
            if " " in matrix[i][j]["number"]:
                return
    exit("Parabens! Você completou o Sudoku!")
