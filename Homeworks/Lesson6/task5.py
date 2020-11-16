class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Пишем ручкой.')


class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашом.')


class Handle(Stationery):
    def draw(self):
        print('Подчеркиваем маркером.')


my_pen = Pen('ручка')
my_pencil = Pencil('карандаш')
my_handle = Handle('маркер')

my_pen.draw()
my_pencil.draw()
my_handle.draw()
