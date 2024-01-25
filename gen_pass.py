#Lista nr 3
#Zad 2
#Filip Kuś
import string
import random


def gen_pass():
    letters = string.ascii_letters + string.digits + string.punctuation
    pass_length = random.randint(8, 16)
    return ''.join(random.choice(letters) for i in range(pass_length))


print(gen_pass())
