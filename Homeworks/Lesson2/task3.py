my_dict = {
    1: 'Зима',
    2: 'Зима',
    3: 'Весна',
    4: 'Весна',
    5: 'Весна',
    6: 'Лето',
    7: 'Лето',
    8: 'Лето',
    9: 'Осень',
    10: 'Осень',
    11: 'Осень',
    12: 'Зима',
}
number_month = int(input('Введите номер месяца : '))
if 1 <= number_month <= 12:
    for key in my_dict:
        if number_month == key:
            print(my_dict.get(key))
            break
        else:
            continue
else:
    print('Введенное число должно быть в диапазоне [1, 12]')


my_list = ['Весна', 'Осень', 'Лето', 'Зима']
number_month_1 = int(input('Введите номер месяца : '))
if 1 <= number_month_1 <= 12:
    if 3 <= number_month_1 <= 5:
        print(my_list[0])
    elif 6 <= number_month_1 <= 8:
        print(my_list[1])
    elif 9 <= number_month_1 <= 11:
        print(my_list[2])
    else:
        print(my_list[3])
else:
    print('Введенное число должно быть в диапазоне [1, 12]')
