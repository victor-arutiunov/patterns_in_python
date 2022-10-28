
class GoldenRing():

    _ring = None

    def __init__(self, owner):
        if self._ring is not None:
            raise ValueError("Ring is already created :(")

        self.owner = owner
        self.__class__._ring = self
    
    @classmethod
    def get_ring(cls):
        if cls._ring is None:
            print("Ring is not created")
            owner: str = input("Create it by your own: ")
            cls._ring = cls(owner)
            return cls._ring
        else:
            return cls._ring
