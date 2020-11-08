from itertools import count, cycle

for el in count(int(input('Введите стартовое число '))):
    print(el)  # беконечный цикл!


my_list = ['Квадрат', 'Треугольник', 404, 505]
for el in cycle(my_list):
    print(el)  # беконечный цикл!
