from homework_14.reader import Reader


class TxtReader(Reader):
    def __init__(self, file_path):
        self.__file_path = file_path

    def read_file(self):
        with open(self.__file_path) as file:
            text = file.read()
        return text
