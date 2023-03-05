from vertebrates import Vertebrates


class Fish(Vertebrates):
    def __init__(self, nutrition: str, move: list):
        super().__init__(nutrition, move)
        self.__gill_bearing = True
        self.__aquatic = True

    @property
    def gill_bearing(self):
        return self.__gill_bearing

    @property
    def aquatic(self):
        return self.__aquatic

    @property
    def breath(self):
        return self.__breath

    @breath.setter
    def breath(self, gill_moves: bool):
        if isinstance(gill_moves, bool) and gill_moves:
            self.__breath = True
        else:
            self.__breath = False


if __name__ == '__main__':
    dori = Fish("carnivorous", ["swim"])
    dori.grow = "Adult"
    print(dori.get_food())
    print(dori.try_to_reproduce())
    dori.breath = True
    print(dori.breath)
