from european_rails import german_rail, france_rail, EuropeanRailway
from american_rails import AmericanRailway


class AdapterAmericanRailwayToEuropean(EuropeanRailway, AmericanRailway):

    def go_to_the_station(self, station):
        self.station_transfer(station)


american_rail = AdapterAmericanRailwayToEuropean(5)


def main():

    railways = [german_rail, france_rail, american_rail]

    for railway in railways:
        railway.go_to_the_station("Cathalonia")


main()
