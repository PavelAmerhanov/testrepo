import json

my_str = {}
average_profit = 0
average_profit_count = 0
with open("5-7.txt", encoding="utf-8") as f_obj:  # под винду7
    for i in f_obj:
        profit = int(i.split()[2]) - int(i.split()[3][:-1])
        my_str[i.split()[0]] = profit
        if profit > 0:
            average_profit += profit
            average_profit_count += 1

my_list = [my_str, {"average_profit": round(average_profit / average_profit_count, 2)}]
print('Итоговый список: ', my_list)

with open('OlegG.json', 'w') as f:  # запишем JSON
    json.dump(my_list, f)
    # print(json.dumps(my_list))

with open('OlegG.json') as f:  # проверим как записалось JSON
    my_list_test = json.load(f)
print('Проверка   JSON: ', my_list_test)
