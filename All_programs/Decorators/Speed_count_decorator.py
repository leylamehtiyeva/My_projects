import time

"""
To calculate the speed of the Euclidean algorithm
"""


def get_gcd(a, b):
    """
    GCD is calculated for natural numbers according to the slow Euclidean algorithm
    :param a: first natural number
    :param b: second natural number
    :return: GCD(a,b)
    """
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    return a


def calculate_time(func):
    """
    Decorator for calculating the speed of the function
    :param func: link to the function we want to decorate
    :return: link to wrapper function
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, *kwargs)
        end_time = time.time()
        dt = end_time - start_time
        print(f'Время работы функции {dt} сек')
        return res
    return wrapper


get_gcd = calculate_time(get_gcd)
res = get_gcd(2, 100000)
print(res)





