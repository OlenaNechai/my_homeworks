from animals import Animals


class Vertebrates(Animals):
    def __init__(self, nutrition: str, move: list):
        super().__init__()
        self.__vertebrae = True
        self.__move = move
        self.__nutrition = nutrition

    @property
    def vertebrae(self):
        return self.__vertebrae

    @property
    def move(self):
        return self.__move

    @property
    def nutrition(self):
        return self.__nutrition

    def get_food(self):
        if self.__nutrition == "carnivorous":
            return f'Do your best {self.__move[0]} to catch your food'
        elif self.__nutrition == "herbivorous":
            return f'{self.__move[0]} around to find your food'

    def try_to_reproduce(self):
        if not self.grow:
            return f'Do your best {self.move[0]} to find a way to reproduce'
        else:
            return 'Your are too young to reproduce'

    def guess_the_class(self):
        if self.__move == ["fly"]:
            return 'You are a bird'
        elif len(self.__move) > 1 and ("swim" in self.__move and "jump" in self.__move and "crawl" in self.__move):
            return 'You must be an amphibian'
        elif self.__move == ["swim"]:
            return 'You are a fish'
        elif len(self.__move) > 1 and ("swim" in self.__move and "crawl" in self.__move and "run" in self.__move):
            return 'You must be a reptile'
        else:
            return 'You must be mammal'


if __name__ == '__main__':
    dori = Vertebrates("carnivorous", ["swim"])
    dori.grow = "Adult"
    print(dori.get_food())
    print(dori.try_to_reproduce())
    print(dori.guess_the_class())
