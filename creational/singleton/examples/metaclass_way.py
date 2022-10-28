
class SingletonMeta(type):
    
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None
    
    def __call__(cls, *args, **kwds):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwds)

        return cls._instance


class Engine(metaclass=SingletonMeta):
    def __init__(self, model):
        self.model = model


e1 = Engine(32)
e2 = Engine(65)

print(e1 is e2)
print(e1.model, e2.model)
