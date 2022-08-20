from copy import deepcopy


class Voyager:
    def __init__(self, name, mission, **kwargs):
        self.name = name
        self.mission = mission
        self.__dict__.update(kwargs)

    def __str__(self):
        return f"Interpalnetary satelite {self.name}, assigned to mission {self.mission} with following configuration {self.__dict__}"

    def copy(self, **kwargs):
        cls = type(self)
        copy_params = deepcopy(self.__dict__)
        copy_params.update(kwargs)
        copy = cls(**copy_params)
        return copy


voyager_1 = Voyager("Voyager 1", "Jupiter-Saturn", camera="8x Sony", cpu="IBM xt98", antena="5.4 MHz")
voyager_2 = voyager_1.copy(name="Voyager 2", mission="Jupiter-Neptune", antena="6.7 MHz", magnicpec="1.2 Fila")

print([voyager_1, voyager_2])
print([voyager_1.__dict__, voyager_2.__dict__])
