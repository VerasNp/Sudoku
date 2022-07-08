import sys

from modules.file import file_exists_list, list_check_ext
from modules.game import start_game, helper
from modules.json import get_json_key_content
from modules.utils import dd


def bootstrapper(args: list = None) -> None:
	try:
		params = args[1:]

		if len(params) >= 3 or len(params) == 0:
			raise Exception(
				get_json_key_content("resources.messages.err.pt_br", "ARGS_WRONG")
			)

		if "-h" in params or "--help" in params:
			helper()
		else:
			file_exists_list(params)

			list_check_ext(params, "txt")

			start_game(params)
	except Exception as e:
		exit(e)


def main() -> None:
	bootstrapper(sys.argv)


if __name__ == "__main__":
	main()
