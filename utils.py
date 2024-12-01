def load_data(path, lines: bool = True):
    with open(path, "r") as file:
        if lines:
            return file.readlines()
        return file.read()
