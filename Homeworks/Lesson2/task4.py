a = input('Введите слова через пробел : ')
my_list = a.split(' ')
for index, el in enumerate(my_list, 1):
    if len(el) >= 10:
        print(index, el[:10])
    else:
        print(index, el)
