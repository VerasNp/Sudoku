import re


def search_data(data, search):
    if search == 'COL':
        return re.search("^[A-I]", data).group(0)
    elif search == 'LIN':
        return re.search(r"[1-9](?=:)", data).group(0)
    elif search == 'NUMBER':
        return re.search(r"[1-9]$", data).group(0)
    else:
        raise Exception('Parâmetro %s não mapeado' % search)


def string_navigation(string: str):
    if not string:
        return
    return string.split(".")
