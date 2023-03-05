# Describe mammals using principles from the lesson. You should implement different fields and methods.
# For example:
# Animals -> mammals -> flying mammals-> Bird -> Eagle
# ............................
# Minimum 3 chains should be implemented
# Classes should be in different modules. You should have at least 5 different classes.

from vertebrates import Vertebrates


class Mammals(Vertebrates):
    def __init__(self, nutrition: str, move: list, fur: bool = None, hair: bool = None):
        super().__init__(nutrition, move)
        self.__producing_milk = True
        self.__has_neocortex = True
        self.__fur = fur
        self.__hair = hair

    @property
    def producing_milk(self):
        return self.__producing_milk

    @property
    def has_neocortex(self):
        return self.__has_neocortex

    @property
    def fur(self):
        return self.__fur

    @property
    def hair(self):
        return self.__hair

    def identify_human(self):
        if self.__hair:
            return f'You must be a human'
        else:
            return f'Hello good animal!'


if __name__ == '__main__':
    dori = Mammals("herbivorous", ["walk", "swim", "run"], hair=True)
    dori.grow = "Adult"
    print(dori.get_food())
    print(dori.try_to_reproduce())
    print(dori.guess_the_class())
    print(dori.identify_human())
