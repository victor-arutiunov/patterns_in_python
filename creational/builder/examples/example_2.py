from enum import Enum
import time


PizzaProgress = Enum("PizzaProgress", "queued, preparation baking ready")
PizzaDough = Enum("PizzaDough", "thin thick")
PizzaSauce = Enum("PizzaSauce", "tomato creme_fraiche hot_tomato")
PizzaToping = Enum("PizzaToping", "mozzarella bacon mashrooms onion oregano ham pineapple")
StepDelay = 3


class Pizza:
    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.toping = []

    def __str__(self):
        return self.name


class MargarittaBuilder:
    def __init__(self):
        self.pizza = Pizza("Margaritta")
        self.progress = PizzaProgress.queued
        self.baking_time = 5

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.dough = PizzaDough.thin

    def add_sauce(self):
        print("Cover your fantastic pizza with my cu... secret sauce")
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(StepDelay)

    def add_toping(self):
        print("Mix of ingredients from all cantons of mother Italy")
        self.pizza.toping = [PizzaToping.mozzarella, PizzaToping.oregano]
        time.sleep(StepDelay)

    def bake(self):
        print(f"Baking for {self.baking_time} minutes...")
        time.sleep(self.baking_time)
        print("Pizza is ready")


class CreamyBaconBuilder:
    def __init__(self):
        self.pizza = Pizza("CreamyBacon")
        self.progress = PizzaProgress.queued
        self.baking_time = 7

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.dough = PizzaDough.thick

    def add_sauce(self):
        print("Adding sauce...")
        self.pizza.sauce = PizzaSauce.creme_fraiche
        time.sleep(StepDelay)

    def add_toping(self):
        print("Adding toping...")
        self.pizza.toping = [toping for toping in PizzaToping]
        time.sleep(StepDelay)

    def bake(self):
        print(f"Baking for {self.baking_time} minutes...")
        time.sleep(self.baking_time)
        print("Pizza is ready")


class HawaiianBuilder(CreamyBaconBuilder):
    def __init__(self):
        self.pizza = Pizza("Hawaiian")
        self.progress = PizzaProgress.queued
        self.baking_time = 6

    def add_toping(self):
        print("Adding toping...")
        self.pizza.toping = [PizzaToping.bacon, PizzaToping.mashrooms, PizzaToping.pineapple, PizzaToping.ham]
        time.sleep(StepDelay)


class Waiter:
    def __init__(self):
        self.builder  = None

    def bake_pizza(self, builder):
        self.builder = builder()

        [step() for step in
        (self.builder.prepare_dough,
         self.builder.add_sauce,
         self.builder.add_toping,
         self.builder.bake)]

    @property
    def pizza(self):
        return self.builder.pizza


def validate_pizza_type(builders):
    try:
        pizza_type = input("What pizza do you like,: \
        [m]argarita, [c]reamy bacon, [h]awaiian?")
        builder = builders[pizza_type]
        return (True, builder)
    except KeyError as err:
        print("This pizza is not available")
        return (True, None)


def main():
    builders: dict = {
        "m": MargarittaBuilder,
        "c": CreamyBaconBuilder,
        "h": HawaiianBuilder,
    }
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_pizza_type(builders)
    print()
    waiter = Waiter()
    waiter.bake_pizza(builder)
    pizza = waiter.pizza
    print(f"Enjoy your fuckin {pizza}, bastard")


if __name__ == "__main__":
    main()
