def sum_of_numbers():
    result = 0
    while True:
        numbers = input('Введите список чисел через пробел  или  q для выхода: ').split()
        for i in numbers:
            try:
                if i == 'q':
                    print('Сумма введенных чисел равна : ', result)
                    return
                else:
                    result += int(i)
            except ValueError:
                print('Введите число или q чтобы выйти')
        print('Сумма введенных чисел равна : ', result)


sum_of_numbers()
