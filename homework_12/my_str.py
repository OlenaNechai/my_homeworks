# Describe any object of your choice in the class.
# I want the object to be printed to the console in the following format:
# class_name: {
#
# key: value
#
# }

class Spring:

    def __init__(self):
        self.__is_here = True

    def __str__(self):
        return f'{self.__class__.__name__}:\n \t {self.__dict__}'


if __name__ == '__main__':
    spring = Spring()
    print(spring)
