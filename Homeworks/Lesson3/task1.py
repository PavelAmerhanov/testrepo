def my_func(dividend, divider):
    error = 'Деление на ноль невозможно'
    if divider == 0:
        return error
    else:
        return round(dividend / divider, 3)


print(my_func(50, 0))
print(my_func(100, 17))
