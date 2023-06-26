class Track:
    def __init__(self, start_x, start_y):
        self.start_x, self.start_y = (start_x, start_y)
        self.line_segment = []

    def add_point(self, x, y, speed):
        self.line_segment.append([(x, y), speed])

    def __getitem__(self, item):
        if isinstance(item, int) and 0 <= item < len(self.line_segment):
            return self.line_segment[item][0]
        else:
            raise IndexError('некорректный индекс')

    def __setitem__(self, key, value):
        if isinstance(key, int) and 0 <= key < len(self.line_segment):
            self.line_segment[key][-1] = value
        else:
            raise IndexError('некорректный индекс')


tr = Track(10, -5.4)
tr.add_point(20, 0, 100)
tr.add_point(50, -20, 80)
tr.add_point(63.45, 1.24, 60.34)

tr[2] = 60
c, s = tr[2]
print(c, s)
print(tr.line_segment)
res = tr[3]