from fish import Fish


class Shark(Fish):
    def __init__(self, name: str, nutrition: str, move: list, cold_blooded: bool, fresh_water: bool):
        super().__init__(nutrition, move)
        self.__name = name
        self.__cold_blooded = cold_blooded
        self.__fresh_water = fresh_water

    @property
    def name(self):
        return self.__name

    @property
    def cold_blooded(self):
        return self.__cold_blooded

    @property
    def fresh_water(self):
        return self.__fresh_water

    def guess_the_shark(self):
        if not self.__cold_blooded and 'white' in self.__name:
            return f'Hello white shark!'
        elif self.__fresh_water and 'bull' in self.__name:
            return f'Hey, glad to see you, bull shark'
        elif 'shark' in self.__name:
            return f'Hey {self.__name}'
        else:
            return f'Are you really a shark?'


if __name__ == '__main__':
    dori = Shark("bull shark", "carnivorous", ["swim"], False, True)
    print(dori.name)
    print(dori.guess_the_shark())
