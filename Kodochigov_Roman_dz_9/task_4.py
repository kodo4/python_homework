class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} Машина поехала'

    def stop(self):
        return f'{self.name} Машина остановилась'

    def turn(self, direction):
        if direction == 'left':
            return f'{self.name} Повернула налево'
        elif direction == 'right':
            return f'{self.name} Повернула направо'

    def show_speed(self):
        return (f'{self.name} На спидометре {self.speed}км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'{self.name} Превышение скорости. На спидометре {self.speed}'
        else:
            return super().show_speed()

class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'{self.name} Превышение скорости. На спидометре {self.speed}'
        else:
            return super().show_speed()


class PoliceCar(Car):
    pass


a = Car(40, 'yellow', 'Mers')
print(a.go())
print(a.show_speed())
print(a.turn('right'))
print(a.stop())
print()
b = TownCar(61, 'red', 'bumbelbi')
print(b.go())
print(b.show_speed())
print(b.turn('left'))
print(b.stop())
print()
c = SportCar(20, 'green', 'buggati')
print(c.go())
print(c.show_speed())
print(c.turn('left'))
print(c.stop())
print()
d = WorkCar(30, 'white', 'мороженка')
print(d.go())
print(d.show_speed())
print(d.turn('left'))
print(d.stop())
print()
police = WorkCar(30, 'blue-white', 'виу-виу', True)
print(police.go())
print(police.show_speed())
print(police.turn('left'))
print(police.stop())
