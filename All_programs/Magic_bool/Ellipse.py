class Ellipse:
    def __init__(self, *args):
        if args:
            self.x1, self.y1, self.x2, self.y2 = args
        self.tp = args

    def __bool__(self):
        return True if self.tp else False

    def get_coords(self):
        if self.tp:
            return self.tp
        else:
            raise AttributeError('No coordinates to retrieve')


lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 1, 2, 2), Ellipse(0, 1, -3, 2)]
lst_geom_filter = list(filter(lambda x: bool(x), lst_geom))
for el in lst_geom_filter:
    el.get_coords()
