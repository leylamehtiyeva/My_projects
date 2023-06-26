import random
from string import ascii_lowercase, ascii_uppercase

# setting the grain of the random number generator
random.seed(1)

# password length
N = 10




def gen():
    chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
    while True:
        a = [chars[random.randint(1, len(chars)) - 1] for i in range(N)]
        yield a


for i in range(5):
    print(''.join(next(gen())))