from itertools import count
from math import factorial


def fact_gen(el):
    yield factorial(el)


def generator():
    g = 0
    while True:
        g += 1
        yield g


number = int(input('Введите число : '))
for j, k in enumerate(generator()):
    print(k)
    if j >= number - 2:
        break

for i, num in enumerate(fact_gen(number)):
    print(num)



