class Cell:
    def __init__(self):
        self.is_free = True
        self.value = 0

    def __bool__(self):
        return self.is_free


class TicTacToe:
    def __init__(self):
        self._n = 3
        self.pole = tuple(tuple(Cell() for _ in range(self._n)) for _ in range(self._n))

    def clear(self):
        for row in self.pole:
            for cell in row:
                cell.is_free = True
                cell.value = 0

    def __check(self, value):
        if type(value) != tuple or len(value) != 2:
            raise IndexError('Invalid cell index')
        if any(not (0 <= x < self._n) for x in value if type(x) != slice):
            raise IndexError('Invalid cell index')

    def __setitem__(self, key, value):
        self.__check(key)
        r, c = key
        if self.pole[r][c]:
            self.pole[r][c].value = value
            self.pole[r][c].is_free = False
        else:
            raise ValueError('Cell is already occupied')

    def __getitem__(self, item):
        self.__check(item)
        r, c = item
        if type(r) == slice:
            return tuple(self.pole[x][c].value for x in range(self._n))
        if type(c) == slice:
            return tuple(self.pole[r][x].value for x in range(self._n))
        return self.pole[r][c].value

