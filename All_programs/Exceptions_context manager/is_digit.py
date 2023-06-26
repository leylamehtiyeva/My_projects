lst = "1 -5.6 True abc 0 23.56 hello".split()


def is_digit(x):
    try:
        return int(x)
    except:
        try:
            return float(x)
        except:
            return x


res = list(map(is_digit, lst))
print(res)