from abc import ABCMeta, abstractmethod
from unicodedata import category


class Component(metaclass=ABCMeta):

    name: str

    @abstractmethod
    def get_name(self, item):
        pass


class Category(Component):
    
    def get_name(self):
        return self.name


class Item(Component):

    def get_name(self):
        return self.name


category = Category()
