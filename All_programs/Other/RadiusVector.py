"""A class RadiusVector for describing and working with an n-dimensional vector (which has n coordinates)"""

class RadiusVector:
    def __init__(self, *args):
        if len(args) == 1:
            self.coords = (0,) * args[0]
        else:
            self.coords = tuple(args)

    def set_coords(self, *args):
        self.coords = tuple(args)

    def get_coords(self):
        return self.coords

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        return sum([i**2 for i in self.coords])**0.5

vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8, 10, 11)
res_len = len(vector3D) # res_len = 3
res_abs = abs(vector3D)
print(res_len, res_abs)





