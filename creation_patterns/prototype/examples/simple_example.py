from copy import deepcopy


class A:
    def __init__(self):
        self.x = 17
        self.first_name = "Ash"


class B(A):
    def __init__(self):
        A.__init__(self)
        self.y = 8
        self.second_name = "Barclaey"

    def __str__(self):
        return f"{self.first_name}, {self.second_name}, {self.x}, {self.y}"


if __name__ == "__main__":
    obj = B()
    obj_copy = deepcopy(obj)
    print([str(i) for i in [obj, obj_copy]])
    print([i for i in [obj, obj_copy]])
