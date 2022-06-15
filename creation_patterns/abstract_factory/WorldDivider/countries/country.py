import random
from pprint import pprint
from abc import ABC, abstractmethod

import yaml


with open("countries.yaml", "r") as f:
    countries = yaml.safe_load(f)
    pprint(countries)


class Country(ABC):
    def __init__(self,
                 name:str,
                 size: int,
                 population: int,
                 army_manpower: int,
                 resources: list,) -> None:
        self.name = name
        self.size = size
        self.population = population
        self.army_manpower = army_manpower
        self.resources = resources

    def action(self) -> None:
        random.choice([self.trade_with(random.choice([countries])),
                       self.announce_war_to(random.choice([countries])),])

    def trade_with(self, country) -> None:
        print(f"{self.name} signed a trade deal with {country.name}")

    def announce_war_to(self, country) -> None:
        print(f"{self.name} announce war to {country.name}")

    def make_peace(self, country) -> None:
        print(f"{self.name} make peace with {country.name}")

    def accept_inner_message(self, type, country) -> None:
        pass
