"""
Need to finish
"""

class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @classmethod
    def verify_var(cls, variable):
        return cls.MIN_DIMENSION <= variable <= cls.MAX_DIMENSION

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.__a = a if self.verify_var(a) else self

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.__b = b if self.verify_var(b) else self

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c):
        self.__c = c if self.verify_var(c) else self

    def __le__(self, other):
        return self.volume() <= other.volume()

    def __lt__(self, other):
        return self.volume() < other.volume()

    def volume(self):
        return self.a * self.b * self.c


lst_shop = [ShopItem('кеды', 1024, Dimensions(40, 30, 120)),
            ShopItem('зонт', 500.24, Dimensions(10, 20, 50)),
            ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)),
            ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))]


lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim.volume())
print(lst_shop_sorted)


