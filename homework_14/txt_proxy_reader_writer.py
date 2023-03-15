from homework_14.txt_reader import TxtReader
from homework_14.txt_writer import TxtWriter


class TxtProxyReaderWriter:
    def __init__(self, file_path: str):
        self.__result = ''
        self.__is_actual = False
        self.__reader = TxtReader(file_path)
        self.__writer = TxtWriter(file_path)

    def read_file(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__reader.read_file()
            self.__is_actual = True
            return self.__result

    def write_file(self, text_to_write: str):
        if self.__result == text_to_write:
            return f'New text is equal to the current text, write operation is cancelled'
        else:
            self.__result = self.__writer.write_file(text_to_write)
            self.__is_actual = True
            return self.__result


if __name__ == '__main__':
    txt_reader = TxtProxyReaderWriter('test.txt')
    print(txt_reader.read_file())
    print('\n')
    print(txt_reader.write_file('TEST!!!'))
    # txt_reader.write_file('***')
    # txt_reader.read_file()
