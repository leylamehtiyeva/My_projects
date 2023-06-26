import math


class Derivative:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.00001, *args, **kwargs):
        return (self.__fn(x+dx) - self.__fn(x)) / dx


@Derivative
def df_sin(x):
    return math.sin(x)


print(df_sin(math.pi/3))
