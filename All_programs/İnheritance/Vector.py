class Vector:
    _allowed_types = (int, float)

    def __init__(self, *args):
        self.__check_coords(args)
        self._coords = args

    def __check_coords(self, coords):
        if not all(type(x) in self._allowed_types for x in coords):
            raise ValueError('wrong type of coordinates')

    def get_coords(self):
        return self._coords

    @staticmethod
    def __is_vector(obj):
        if not isinstance(obj, Vector):
            raise TypeError("Operand must be an object of class vector")

    def __check_vector_dims(self, other):
        if len(self._coords) != len(other.get_coords()):
            raise TypeError('The dimensions of the vectors do not match')

    def _make_vector(self, coords):
        try:
            return self.__class__(*coords)
        except ValueError:
            return Vector(*coords)

    def __add__(self, other):
        self.__is_vector(other)
        self.__check_vector_dims(other)
        coords = tuple(a + b for a, b in zip(self._coords, other.get_coords()))
        return self._make_vector(coords)

    def __sub__(self, other):
        self.__is_vector(other)
        self.__check_vector_dims(other)
        coords = tuple(a - b for a, b in zip(self._coords, other.get_coords()))
        return self._make_vector(coords)


class VectorInt(Vector):
    _allowed_types = (int,)


v1 = VectorInt(1, 2, 3, 7)
v2 = VectorInt(1, 2, 0, 4.6)
v = v1 + v2
print(v.coord)
