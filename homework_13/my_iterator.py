# Create an iterator that accepts a sequence and can iterate over values in a given range.
# CustomIterator(sequence, start_index, end_index)

from typing import Union


class CustomIterator:

    def __init__(self, sequence: Union[str, list, tuple, dict], start_index: int, end_index: int):
        self.__sequence = sequence
        self.__start_index = start_index
        self.__end_index = end_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.__start_index < self.__end_index:
            value = self.__sequence[self.__start_index]
            self.__start_index += 1
            return value
        else:
            raise StopIteration


if __name__ == '__main__':
    my_iterator = CustomIterator('hello world', 0, 11)
    for item in my_iterator:
        print(item)
