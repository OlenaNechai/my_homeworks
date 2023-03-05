from birds import Birds


class Penguin(Birds):
    def __init__(self, name: str, nutrition: str, move: list, season: str):
        Birds.__init__(self, nutrition, move, season)
        self.__feather = True
        self.__toothless = True
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def feather(self):
        return self.__feather

    @property
    def toothless(self):
        return self.__toothless

    def be_happy_to_swim(self):
        if 'penguin' in self.name:
            return f'{self.name} are swimming birds!'
        else:
            return f'Hello nice bird!'


if __name__ == '__main__':
    dori = Penguin("Emperor penguin", "carnivorous", ["swim"], season="spring")
    print(dori.name)
    dori.grow = "Adult"
    print(dori.get_food())
    print(dori.try_to_reproduce())
    print(dori.be_happy_to_swim())
