class Furniture:
    def __init__(self, name, weight):
        self.__verify_name()
        self._name = name
        self.__verify_weight()
        self._weight = weight

    def __verify_name(self):
        if not isinstance(self._name, str):
            raise TypeError('Value must be str')

    def __verify_weight(self):
        if not isinstance(self._weight, int) and not self._weight > 0:
            raise TypeError('Weight must be a positive number')

    def get_attrs(self):
        return tuple(self.__dict__)


class Closet(Furniture):
    def __init__(self, name, weight, tp, doors):
        Furniture.__init__(self, name, weight)
        self._tp = tp
        self._doors = doors


class Chair(Furniture):
    def __init__(self, name, weight, height):
        Furniture.__init__(self, name, weight)
        self.height = height


class Table(Furniture):
    def __init__(self, name, weight, height, square):
        Furniture.__init__(self, name, weight)
        self._height = height
        self._square = square


cl = Closet('шкаф-купе', 342.56, True, 3)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)
print(tb.get_attrs())
