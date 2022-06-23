from modules.validators import validate_input


def start_interactive_mode():
    while True:
        try:
            entry = input()
            validate_input(entry, "resources.messages.err.pt_br.INPUT", True)
            print(entry)
        except EOFError:
            print("Tchau :)")
            break
        except Exception as e:
            print(e)
