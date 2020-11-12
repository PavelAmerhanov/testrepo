my_f = open("5-1.txt", "w", encoding="utf-8")  # перезатрем если есть такой файл
while True:
    my_str = input('Введите строку, если закончили просто нажмите ВВОД: ')
    my_f.write(my_str + '\n')  # добавим знак /n чтобы красивее гляделось
    if my_str == '':
        break

my_f.close()
