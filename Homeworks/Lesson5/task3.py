with open("5-3.txt", encoding="utf-8") as f_obj:
    count = 0  # счетчик количества строк
    amount = 0  # сумма всех зарплат
    for i in f_obj:
        count += 1
        amount += int(i.split()[1])
        if int(i.split()[1]) < 20000:
            print(i.split()[0])

print('Средняя ЗП = ', amount / count)
