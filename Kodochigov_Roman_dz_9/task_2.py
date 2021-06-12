class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_weight(self):
        weight = self._length * self._width * 25 * 5
        return f'{weight}кг'


a = Road(20, 5000)
print(a.calc_weight())
