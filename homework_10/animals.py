from abc import ABC, abstractmethod


class Animals(ABC):
    def __init__(self):
        self.__breath = True
        self.__reproduce = True
        self.__grow = True

    @property
    def grow(self):
        return self.__grow

    @grow.setter
    def grow(self, phase_of_life: str):
        if phase_of_life == "Adult":
            self.__grow = False

    @property
    def breath(self):
        return self.__breath

    @breath.setter
    def breath(self, number_of_inhales_exhales: int):
        if number_of_inhales_exhales == 0:
            self.__breath = False

    @property
    def reproduce(self):
        return self.__reproduce

    @abstractmethod
    def get_food(self):
        pass

    @abstractmethod
    def try_to_reproduce(self):
        pass
