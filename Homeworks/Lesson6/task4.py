class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police  # Булево

    def go(self):
        print('машина поехала')

    def stop(self):
        print('машина остановилась')

    def turn(self, direction):
        print(F'машина повернула {direction}')

    def show_speed(self):
        print(F'Скорость астомобиля {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print(F'Скорость городского астомобиля {self.speed}')
        if self.speed > 60:
            print(F'Внимание вы первысили скорость на {self.speed - 60} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self, speed):
        self.speed = speed
        print(F'Скорость городского автомобиля {self.speed}')


class PoliceCar(Car):
    pass


t_car = TownCar(65, 'Зеленый', 'Еда', False)
t_car.show_speed()

p_car = PoliceCar(90, 'Голубой', 'Джип', True)
if p_car.is_police:
    print(F'Машина {p_car.color}, {p_car.name} является полицейской машиной')
else:
    print(F'Машина {p_car.color} цвет, {p_car.name} Не является полицейской машиной')

s_car = SportCar(110, 'Красный', 'бензин', False)

print(F'У нас машина {s_car.color} цвет, {s_car.name}:')
s_car.go()
s_car.turn('Налево')
