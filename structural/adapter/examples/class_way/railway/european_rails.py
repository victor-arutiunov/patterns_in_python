from abc import ABC, ABCMeta


class EuropeanRailway(metaclass=ABCMeta):

    rail_width: int = 5

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


german_rail = GermanRailway()
france_rail = FranceRailway()
