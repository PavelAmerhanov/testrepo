time_in_sec = int(input('Введите время в секундах : '))
hours = time_in_sec // 60 // 60
minutes = time_in_sec // 60 % 60
sec = time_in_sec % 60 % 60
print(f'{hours}:{minutes}:{sec}')
