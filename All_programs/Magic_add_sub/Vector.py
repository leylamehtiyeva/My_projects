class Vector:
    def __init__(self, *args):
        self.coords = args

    def check_length(self, tp1, tp2):
        if len(tp1) != len(tp2):
            raise ArithmeticError('размерности векторов не совпадают')

    def __add__(self, other):
        self.check_length(self.coords, other.coords)
        return Vector(*(self.coords[i] + other.coords[i] for i in range(len(self.coords))))

    def __sub__(self, other):
        self.check_length(self.coords, other.coords)
        return Vector(*(self.coords[i] - other.coords[i] for i in range(len(self.coords))))

    def __mul__(self, other):
        self.check_length(self.coords, other.coords)
        return Vector(*(self.coords[i] * other.coords[i] for i in range(len(self.coords))))

    def __iadd__(self, other):
        elem = other
        if type(elem) == int:
            return (self.coords[i] + elem for i in range(len(self.coords)))
        else:
            return self + elem


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v1 += 10
print(v1.coords)
