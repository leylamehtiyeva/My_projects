class RadiusVector:
    def __init__(self, *args):
        self.coords = list(args)

    def __getitem__(self, item):
        return tuple(self.coords[item]) if type(item) == slice else self.coords[item]

    def __setitem__(self, key, value):
        self.coords[key] = value


v = RadiusVector(1, 2, 3, 4, 5)
coord = v[2]
print(v.coords[1:4])