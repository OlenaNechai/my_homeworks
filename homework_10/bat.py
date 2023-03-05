from mammals import Mammals


class Bat(Mammals):
    def __init__(self, name: str, nutrition: str, move: list, fur: str = None):
        super().__init__(nutrition, move)
        self.__name = name
        self.__fur = fur

    @property
    def name(self):
        return self.__name

    @property
    def fur(self):
        return self.__fur

    def be_happy_to_fly(self):
        if 'bat' in self.name:
            return f'{self.name} are flying mammals!'
        else:
            return f'Hello good mammal!'

    def make_compliment(self):
        if isinstance(self.__fur, str):
            return f'You {self.__fur} is very beautiful'
        else:
            return f'You are beautiful'


if __name__ == '__main__':
    dori = Bat("New Zealand short-tailed bats", "herbivorous", ["fly"], fur="black fur")
    print(dori.name)
    dori.grow = "Adult"
    print(dori.get_food())
    print(dori.try_to_reproduce())
    print(dori.be_happy_to_fly())
    print(dori.make_compliment())
