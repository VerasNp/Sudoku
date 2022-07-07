import sys

from modules.file import file_exists_list, check_ext_list
from modules.game import start_game, helper
from modules.json import get_json_key_content


def bootstrapper(args: list = None) -> None:
	"""
	Initiates the Sudoku game
	:param args:
	:return:
	"""
	try:
		args_copy = args[1:]

		if len(args_copy) >= 3 or len(args_copy) == 0:
			raise Exception("\033[1;31m" + get_json_key_content("resources.messages.err.pt_br", "ARGS_WRONG"))

		if "-h" in args_copy or "--help" in args_copy:
			helper()
		else:
			file_exists_list(args_copy)

			check_ext_list(args_copy, "txt")

			start_game(args_copy)
	except Exception as e:
		exit(e)


def main() -> None:
	bootstrapper(sys.argv)


if __name__ == "__main__":
	main()
