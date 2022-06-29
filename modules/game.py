from modules.interactive_mode import start_interactive_mode
from modules.matrix import init_matrix


def start_game(data: list) -> None:
    """
    Based in the quantity of args selects the game mode
    :param data:
    :return:
    """
    matrix = init_matrix(9, 9, {"number": ' ', "hint": None})
    if len(data) > 1:
        return
    else:
        start_interactive_mode(matrix, data)