class ListMath:
    def __init__(self, lst=None):
        self.lst_math = [x for x in lst if type(x) in (int, float)] if lst and type(lst) == list else []

    @staticmethod
    def verify_value(value):
        if not type(value) in (int, float):
            raise ArithmeticError('The number must be int or float')

    def __add__(self, other):
        self.verify_value(other)
        return ListMath([x + other for x in self.lst_math])

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.verify_value(other)
        self.lst_math = [x + other for x in self.lst_math]
        return self

    def __sub__(self, other):
        self.verify_value(other)
        return ListMath([x - other for x in self.lst_math])

    def __rsub__(self, other):
        return ListMath([other - x for x in self.lst_math])

    def __isub__(self, other):
        self.verify_value(other)
        self.lst_math = [x - other for x in self.lst_math]
        return self

    def __mul__(self, other):
        self.verify_value(other)
        return ListMath([x * other for x in self.lst_math])

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        self.verify_value(other)
        self.lst_math = [x * other for x in self.lst_math]
        return self

    def __truediv__(self, other):
        self.verify_value(other)
        return ListMath([x / other for x in self.lst_math])

    def __rtruediv__(self, other):
        return self / other

    def __itruediv__(self, other):
        self.verify_value(other)
        self.lst_math = [x / other for x in self.lst_math]
        return self


lst = ListMath([1, "abc", -5, 7.68, True])
lst = lst + 76 # сложение каждого числа списка с определенным числом
lst = 6.5 + lst # сложение каждого числа списка с определенным числом
lst += 76.7  # сложение каждого числа списка с определенным числом
lst = lst - 76 # вычитание из каждого числа списка определенного числа
lst = 7.0 - lst # вычитание из числа каждого числа списка
lst -= 76.3
lst = lst * 5 # умножение каждого числа списка на указанное число (в данном случае на 5)
lst = 5 * lst # умножение каждого числа списка на указанное число (в данном случае на 5)
lst *= 5.54
lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
lst = 3 / lst # деление числа на каждый элемент списка
lst /= 13.0
