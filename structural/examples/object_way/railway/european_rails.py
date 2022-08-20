from abc import ABC, ABCMeta


class EuropeanRailway(metaclass=ABCMeta):

    def __init__(self, rail_width):
        if rail_width != 5:
            raise ValueError("This rail width is not supported by our network")
        self.rail_width = rail_width

    def go_to_the_station(self):
        """release some method in child classes"""


class GermanRailway(EuropeanRailway):

    @staticmethod
    def go_to_the_station(station):
        print(f"Relaxing travel to the {station} station")


class FranceRailway(EuropeanRailway):

    @staticmethod
    def go_to_the_station(station):
        print(f"Croissant travel to the {station} station")


german_rail = GermanRailway(5)
france_rail = FranceRailway(5)
