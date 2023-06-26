

def get_simple_num():
    num = 2
    while True:
        flag = True
        for i in range(2, num):
            if num%i==0:
                flag = False
                break
        if flag:
            yield num
        num +=1

a = get_simple_num()

for i in range(5):
    print(next(a), end = ' ')