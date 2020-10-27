revenue = int(input('Введите выручку : '))
cost = int(input('Введите издержки : '))
if revenue <= cost:
    print('Фирма работает в убыток')
else:
    print('Фирма работает с прибылью')
    revenue_margin = int(((revenue - cost) / revenue) * 100)
    print(f'Рентабельность фирмы {revenue_margin} %')
    number_of_employees = int(input('Введите колличество сотрудников в фирме : '))
    profit_per_employee = int((revenue - cost) / number_of_employees)
    print(f'Прибыль фирмы на одного сотрудника равна : {profit_per_employee}')
