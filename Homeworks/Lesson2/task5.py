my_list = [7, 5, 3, 3, 2]
natural_number = int(input('Введите натуральное число : '))
counter = 0
for el in my_list:
    counter += 1
    if el == natural_number:
        my_list.insert((my_list.index(el)), natural_number)
        print(my_list)
        break
    elif counter == len(my_list):
        if natural_number >= my_list[0]:
            my_list.insert(0, natural_number)
            print(my_list)
            break
        else:
            my_list.append(natural_number)
            print(my_list)
            break
