def get_loss(w1, w2, w3, w4):
    try:
        s = 10 * w1 // w2
    except:
        return "деление на ноль"
    else:
        y = s - 5 * w2 * w3 + w4
        return y


print(get_loss(1, 2, 3, 4))



