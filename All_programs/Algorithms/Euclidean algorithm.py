import time

""""To find the greatest common divisor"""

"""-------------------------------Slow algorithm---------------------------------------"""


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


def test_gcd(func):
    # -----test 1------
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print('Test 1 passed successfully')
    else:
        print('Test 1 failed')

    # -----test 2------
    a = 100
    b = 1
    res = func(a, b)
    if res == 1:
        print('Test 2 passed successfully')
    else:
        print('Test 2 failed')

    # -----test 3------
    a = 2
    b = 100000000
    start = time.time()
    res = func(a, b)
    end = time.time()
    dt = end - start
    if res == 2 and dt < 1:
        print('Test 3 passed successfully')
    else:
        print('Test 3 failed')


# test_gcd(get_gcd)


"""-------------------------------Fast algorithm---------------------------------------"""


def get_gcd_fast(a, b):
    """
    GCD is calculated for natural numbers according to the fast Euclidean algorithm
    :param a: first natural number
    :param b: second natural number
    :return: GCD(a,b)
    """
    # take b as the smaller variable
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a


test_gcd(get_gcd_fast)
