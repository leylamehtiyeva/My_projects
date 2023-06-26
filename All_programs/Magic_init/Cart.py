class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f"{obj.name}: {obj.price}" for obj in self.goods]


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
cart.add(TV('LG', 1000))
cart.add(TV('Hoot', 1000))
cart.add(Table('Hoof', 1000))
cart.add(Notebook('LG', 1000))
cart.add(Notebook('Lk', 1000))
cart.add(Cup('Lq', 1000))


