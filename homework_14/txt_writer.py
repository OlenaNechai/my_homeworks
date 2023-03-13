from homework_14.writer import Writer


class TxtWriter(Writer):
    def __init__(self, file_path):
        self.__file_path = file_path

    def write_file(self, new_data: str):
        with open(self.__file_path, 'w') as file:
            text = file.write(new_data)
        return text
