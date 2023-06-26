class Tuple(tuple):
    def __add__(self, other):
        if not isinstance(other, tuple):
            return tuple(self) + tuple(other)
        return tuple(self) + other


print(isinstance(2, ))