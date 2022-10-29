from __future__ import annotations
from abc import ABCMeta, abstractmethod


class Composite(metaclass=ABCMeta):
    name: str
    parent: str | None = None

    def __init__(self, name: str = ""):
        self.name = name

class Category(Composite):
    children: list = []

    @property
    def components(self) -> list:
        component:  list = self.children
        return component

    @property
    def items(self) -> list:
        items: list = [item for item
                       in self.children
                       if item.__class__ is Item]
        return items

    @property
    def subcategories(self) -> list:
        subcategories: list = [subcategory for subcategory
                               in self.children
                               if subcategory.__class__ is Category]
        return subcategories

    def _get_by_type(self, name: str, composite_type: type) -> Category | Item:
        components: list[Item | Category] = [component for component
                                             in self.children
                                             if component.__class__ is composite_type
                                             and component.name == name]

        if (len(components) == 0):
            return None

        component: Composite = components[0]
        return component

    def get_item(self, name: str) -> Item | None:
        item: Item | None = self._get_by_type(name, Item)
        return item

    def get_subcategory(self, name: str) -> Category | None:
        subcategory: Category | None = self._get_by_type(name, Category)
        return subcategory

    def add_item(self, name: str) -> None:
        item: Item = Item(name)
        item.parent = self
        self.children.append(item)

    def add_subcategory(self, name: str) -> None:
        subcategory: subcategory = Category(name)
        subcategory.parent = self
        self.children.append(subcategory)



class Item(Composite):
    pass


category = Category("main")

items: list = ['name11', 'name5', 'name5']
subcategories: list = ['subcat11', 'subcat5', 'subcat5']

for item in items:
    category.add_item(item)

for subcategory in subcategories:
    category.add_subcategory(subcategory)
