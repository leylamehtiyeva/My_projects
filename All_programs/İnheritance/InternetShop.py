import itertools


class Thing:
    id_generator = itertools.count()
    __attrs = ('id', 'name', 'price', 'weight', 'dims', 'memory', 'frm')

    def __init__(self, name, price):
        self.id = self.__get_id()
        self.name = name
        self.price = price
        self.weight = self.dims = self.memory = self.frm = None

    @classmethod
    def __get_id(cls):
        return next(cls.id_generator)

    def get_data(self):
        return tuple(getattr(self, el) for el in self.__attrs)


class Table(Thing):
    def __init__(self, name, price, weight, dims):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing):
    def __init__(self, name, price, memory, frm):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm


table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(book.get_data())

