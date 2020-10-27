first_distance = int(input('Сколько километров пробежал спортсмен в первый день : '))
count_distance = int(input('Сколько километров спортсмен должен пробежать : '))
print('Результат :')
count_days = 1
print(f'{count_days}й день: %.2f' % first_distance)
while first_distance <= count_distance:
    first_distance = (first_distance * 0.1) + first_distance
    count_days += 1
    print(f'{count_days}й день: %.2f' % first_distance)
print(f'Ответ: на {count_days}й день спортсмен достиг результата — не менее {count_distance} км.')
