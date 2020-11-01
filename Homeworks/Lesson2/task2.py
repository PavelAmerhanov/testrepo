my_list = list(input('Введите элементы списка без пробела, по окончании нажмите Enter : '))
print(my_list)
for i, el in enumerate(my_list):
    if i == (len(my_list) - 1):
        break
    else:
        if i % 2 != 0:
            continue
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print(my_list)
