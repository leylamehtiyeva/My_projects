class Triangle:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
        if not all(map(lambda x: type(x) in (int, float) and x >= 0, (a, b, c))):
            raise TypeError('Triangle sides must be positive numbers')
        elif 2 * max(a, b, c) > a + b + c:
            raise ValueError('The given side lengths cannot form a triangle')


input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2),
              (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]

lst_tr = []
for obj in input_data:
    try:
        lst_tr.append(Triangle(*obj))
    except TypeError:
        continue
    except ValueError:
        continue

print(lst_tr)
