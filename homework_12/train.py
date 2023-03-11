class Train:
    def __init__(self):
        self.__locomotive = '<=[HEAD]'
        self.__wagons = dict()

    def __len__(self):
        return len(self.__wagons)

    def __setitem__(self, key, value):
        self.__wagons[key] = value

    def __getitem__(self, item):
        return self.__wagons[item]

    def form_the_train(self):
        whole_train = self.__locomotive
        for key, value in self.__wagons.items():
            whole_train += f'-{self.__wagons[key]}'
        return whole_train
