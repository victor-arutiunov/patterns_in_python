from abc import ABC, abstractmethod


class RAM(ABC):
    type = None

    def __str__(self):
        return f"{self.type} RAM with {self.amount}GB amount of memory"


class DDR3RAM(ABC):
    type = "DDR3"

    def __init__(self, amount):
        self.amount: int = amount

    def __str__(self):
        return f"{self.type} RAM with {self.amount}GB amount of memory"


class DDR4RAM(ABC):
    type = "DDR4"

    def __init__(self, amount):
        self.amount: int = amount

    def __str__(self):
        return f"{self.type} RAM with {self.amount}GB amount of memory"


class Monitor(ABC):
    type = None

    def __str__(self):
        return f"{self.type} monitor with {self.resolution} resolution"


class OLEDMonitor(Monitor):
    type = "OLED"

    def __init__(self, resolution):
        self.resolution = resolution

    def __str__(self):
        return f"{self.type} monitor with {self.resolution} resolution"


class AMOLEDMonitor(Monitor):
    type = "AMOLED"

    def __init__(self, resolution):
        self.resolution = resolution

    def __str__(self):
        return f"{self.type} monitor with {self.resolution} resolution"


class LaptopComponentsAbstractFactory(ABC):

    @abstractmethod
    def produce_ram(self, amount, type):
        """Produce RAM"""

    @abstractmethod
    def produce_monitor(self, resolution, type):
        """Produce Monitor"""


class ASUSLaptopComponentsFactory(LaptopComponentsAbstractFactory):

    def produce_ram(self, amount):
        return DDR3RAM(amount)

    def produce_monitor(self, resolution):
        return OLEDMonitor(resolution)


class ACERLaptopComponentsFactory(LaptopComponentsAbstractFactory):

    def produce_ram(self, amount):
        return RAM(amount)

    def produce_monitor(self, resolution):
        return AMOLEDMonitor(resolution)


asus_factory = ASUSLaptopComponentsFactory()
acer_factory = ACERLaptopComponentsFactory()


ram = asus_factory.produce_ram(8)
monitor = acer_factory.produce_monitor('4k')

print(ram, monitor)
