class Wagon:
    def __init__(self, number: int, passengers: list):
        self.__number = number
        self.__passengers = passengers

    def __len__(self):
        return len(self.__passengers)

    def __str__(self):
        return f'[{self.__number}]'

    def __add__(self, passenger):
        return self.__passengers.append(passenger)

