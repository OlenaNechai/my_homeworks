from vertebrates import Vertebrates


class Birds(Vertebrates):
    def __init__(self, nutrition: str, move: list, season: str):
        super().__init__(nutrition, move)
        self.__feather = True
        self.__toothless = True
        self.__season = season

    @property
    def feather(self):
        return self.__feather

    @property
    def toothless(self):
        return self.__toothless

    @property
    def season(self):
        return self.__season

    @season.setter
    def season(self, current_season: str):
        if isinstance(current_season, str) and current_season in ("winter", "spring", "summer", "autumn"):
            self.__season = current_season

    @property
    def grow(self):
        return self.__grow

    @grow.setter
    def grow(self, phase_of_life: str):
        if phase_of_life == "Adult":
            self.__grow = False

    def try_to_reproduce(self):
        if not self.__grow and self.__season == 'spring':
            return f'Do your best {self.move[0]} to lay some hard-shelled eggs'
        elif not self.__grow and self.__season != 'spring':
            return f'Wait for the spring!'
        else:
            return 'Your are too young to reproduce'


if __name__ == '__main__':
    dori = Birds("carnivorous", ["fly"], season="spring")
    dori.grow = "Adult"
    print(dori.get_food())
    print(dori.try_to_reproduce())
