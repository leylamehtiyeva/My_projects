class Rect:
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def __setattr__(self, key, value):
        if type(value) not in (int, float):
            raise ValueError('incorrect coordinates and rectangle parameters')
        if key in ('_width', '_height') and value <= 0:
            raise ValueError('incorrect coordinates and rectangle parameters')

        object.__setattr__(self, key, value)

    def is_collision(self, rect):
        if not isinstance(rect, Rect):
            raise TypeError('The argument must be an object of class Rect')

        if not (self._x + self._width < rect._x or rect._x + rect._width < self._x or
                self._y + self._height < rect._y or rect._y + rect._height < self._y):
            raise TypeError('rectangles intersect')


def is_collision(r1, r2):
    try:
        r1.is_collision(r2)
    except TypeError:
        return True
    return False


lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]
lst_not_collision = [lst_rect[i] for i in range(len(lst_rect))
                    if not any(is_collision(lst_rect[i], lst_rect[j]) for j in range(len(lst_rect)) if i != j)]

print(lst_not_collision)




