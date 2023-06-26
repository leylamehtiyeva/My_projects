class Point:
    def __init__(self, *args):
        self._x, self._y = args if args else (0, 0)


try:
    x, y = map(int, input().split())
    pt = Point(x, y)
except:
    try:
        x, y = map(float, input().split())
        pt = Point(x, y)
    except:
        pt = Point()
finally:
    print(f"Point: x = {pt._x}, y = {pt._y}")



