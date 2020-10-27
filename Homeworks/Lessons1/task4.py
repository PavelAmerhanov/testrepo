number = int(input('Введите целое положительное число: '))
count = 0  # количество разрядов
max_number = 0  # максимальная цифра в числе
variable_of_digits = 0  # переменная для  проверки цифр из числа
count_number = number
while count_number > 0:
    count_number = count_number // 10
    count = count + 1
a = 0  # счетчик
while count > 0:
    if a == 0:
        variable_of_digits = number // (10 ** (count - 1))
        if variable_of_digits > max_number:
            max_number = variable_of_digits
            count = count - 1
        a = a + 1
    if count > 1:
        variable_of_digits = (number // (10 ** (count - 1)) % 10)
        if variable_of_digits > max_number:
            max_number = variable_of_digits
        count = count - 1
        continue
    variable_of_digits = number % 10
    if variable_of_digits > max_number:
        max_number = variable_of_digits
    count = count - 1
print(max_number)
