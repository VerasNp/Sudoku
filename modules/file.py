import os.path


def read_file(file):
    content = []
    with open(file) as f:
        while True:
            line = f.readline()
            if not line:
                break
            else:
                content.append(line.rstrip())
    return content


def file_exists(file):
    if os.path.isfile(file):
        return
    else:
        exit("O arquivo " + file + " não existe!")


def file_is_txt(file):
    if os.path.splitext(file)[1] == ".txt":
        return
    else:
        exit("O arquivo " + file + " tem extensão não válida para execução!")


def get_json_path(data):
    data.pop(len(data) - 1)
    data[len(data) - 1] = data[len(data) - 1] + ".json"
    path = ""
    for i in data:
        path += i + "/"
    path = path[:-1]
    file_exists(path)
    return path
