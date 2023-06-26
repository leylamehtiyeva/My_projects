"""The PolyLine class is for represent a line from a sequence of straight line segments."""

class PolyLine:
    def __init__(self, start_coord, *args):
        # start_coord and args = (x, y)
        self.coords = []
        self.coords.append(start_coord)
        for coord in args:
            self.coords.append(coord)

    def add_coord(self, x, y):
        if (x, y) not in self.coords:
            self.coords.append((x, y))

    def remove_coord(self, indx):
        self.coords.pop(indx)

    def get_coords(self):
        return self.coords

poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
poly.add_coord(4,5)
poly.remove_coord(2)
poly.get_coords()
print(poly.get_coords())




