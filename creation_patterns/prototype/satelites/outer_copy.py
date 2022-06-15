from copy import deepcopy


class Voyager:
    def __init__(self, name, mission, **kwargs):
        self.name = name
        self.mission = mission
        self.__dict__.update(kwargs)

    def __str__(self):
        return f"Interpalnetary satelite {self.name}, assigned to mission {self.mission} with following configuration {self.__dict__}"


class SateliteCopier:
    def __init__(self):
        self.satelites = {}

    def register_satelite(self, id, obj):
        self.satelites[id] = obj

    def unregister_satelite(self, id):
        del self.satelites[id]

    def make_copy(self, id, **kwargs):
        requested_satelite = self.satelites.get(id)
        if not requested_satelite:
            raise ValueError(f"Satelite {id} is not registered")
        new_satelite = deepcopy(requested_satelite)
        new_satelite.__dict__.update(kwargs)
        return new_satelite


voyager_1 = Voyager("Voyager 1", "Jupiter-Saturn", camera="8x Sony", cpu="IBM xt98", antena="5.4 MHz")

satelite_copier = SateliteCopier()
satelite_copier.register_satelite("432432", voyager_1)

voyager_2 = satelite_copier.make_copy("432432", name="Voyager 2", mission="Jupiter-Neptune", antena="6.7 MHz", magnicpec="1.2 Fila")

print([voyager_1, voyager_2])
print([voyager_1.__dict__, voyager_2.__dict__])
