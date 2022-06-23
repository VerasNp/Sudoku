import sys
from modules.interactive_mode import start_interactive_mode
from modules.validators import validate_input
from modules.file import read_file, file_exists, file_is_txt


def bootstrapper(args=None):
    try:
        aux = args[1:]
        if len(aux) > 1:
            return
        else:
            file_exists(aux[0])
            file_is_txt(aux[0])
            content = read_file(aux[0])
            validate_input(
                content, "resources.messages.err.pt_br.HINT_FILE", True)
            start_interactive_mode()
    except Exception as e:
        exit(e)


def main():
    bootstrapper(sys.argv)


if __name__ == "__main__":
    main()
