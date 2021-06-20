class Stationery:
    def __init__(self, title=None):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Рисуем ручкой'


class Pencil(Stationery):
    def draw(self):
        return f'Рисуем карандашом'


class Handle(Stationery):
    def draw(self):
        return f'Рисуем маркером'


a = Pen()
print(a.draw())
b = Pencil()
print(b.draw())
c = Handle()
print(c.draw())
