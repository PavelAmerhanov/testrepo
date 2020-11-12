def sum_str(temp_str):  # подсчитывает сумму всех чисел в строке
    my_sum = 0
    for el in temp_str.split('(')[:-1]:
        my_sum += int(el.rsplit(' ', 1)[1])

    return my_sum


my_str = {}
with open("5-6.txt", encoding="utf-8") as f_obj:
    for el in f_obj:
        my_str[el.split()[0]] = sum_str(el)

print(my_str)
