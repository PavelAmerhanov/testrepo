from sys import argv

param = argv
try:
    time = int(param[1])
    rate_per_hour = int(param[2])
    bonus = int(param[3])
    salary = time * rate_per_hour + bonus
    print(f'Заработная плата сотрудника  {salary}')
except ValueError:
    print('Вы ввели не число')
