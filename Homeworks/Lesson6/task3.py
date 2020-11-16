class Worker():
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position  # (должность)
        self._income = income  # (доход)


class Position(Worker):
    def get_full_name(self):
        print(F' Полное имя {self.name} {self.surname}')

    def get_total_income(self):
        print(F' Совокупный доход {self._income["wage"] + self._income["bonus"]}')


name1 = Position('Имя1', 'Фам1', 'начальник1', {"wage": 30000, "bonus": 10000})
name1.get_full_name()
name1.get_total_income()

name2 = Position('Имя2', 'Фам2', 'рабочий1', {"wage": 15000, "bonus": 3000})
name2.get_full_name()
name2.get_total_income()
