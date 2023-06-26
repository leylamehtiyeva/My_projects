class SingletonFive:
    _counter = 0
    _link = None

    def __new__(cls, *args, **kwargs):
        if cls._counter < 5:
            cls._link = super().__new__(cls)
            cls._counter += 1

        return cls._link

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]
print(objs)