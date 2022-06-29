import sys

from config import set_environment
from modules.file import file_exists_list, check_ext_list
from modules.game import start_game
from modules.json import get_json_key_content


def bootstrapper(args: list = None) -> None:
    """
    Initiates the sudoku
    :param args:
    :return:
    """
    try:
        set_environment()

        args_copy = args[1:]

        if len(args_copy) >= 3 or len(args_copy) == 0:
            raise Exception(get_json_key_content("resources.messages.err.pt_br", "ARGS_WRONG"))

        file_exists_list(args_copy)

        check_ext_list(args_copy, "txt")

        start_game(args_copy)
    except Exception as e:
        exit(e)


def main() -> None:
    bootstrapper(sys.argv)


if __name__ == "__main__":
    main()
