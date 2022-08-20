from european_rails import german_rail, france_rail, EuropeanRailway
from american_rails import american_rail


class AdapterAmericanRailwayToEuropean(EuropeanRailway):

    american_rail = american_rail

    def go_to_the_station(self, station):
        self.american_rail.station_transfer(station)


adapted_american_rail = AdapterAmericanRailwayToEuropean(5)


def main():

    railways = [german_rail, france_rail, adapted_american_rail]

    for railway in railways:
        railway.go_to_the_station("Cathalonia")


main()
