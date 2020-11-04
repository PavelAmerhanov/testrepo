def my_func(name, surname, year_of_birth, city_of_residence, mail, tele):
    output_person_func = f"{name} {surname} {year_of_birth} {city_of_residence} {mail} {tele}"
    return output_person_func


name_1 = input('Введите свое имя : ')
surname_1 = input('Введите свою фамилию : ')
year_of_birth_1 = input('В каком году вы родились : ')
city_of_residence_1 = input('В каком городе вы живете : ')
mail_1 = input('Введите mail : ')
tele_1 = input('Введите номер телефона : ')
output_person = my_func(name_1, surname_1, year_of_birth_1, city_of_residence_1, mail_1, tele_1)
print(output_person)
