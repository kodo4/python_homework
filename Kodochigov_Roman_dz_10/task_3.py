class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return f'{self.cell}'

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        if self.cell > other.cell:
            return Cell(self.cell - other.cell)
        else:
            return f'Отрицательное количество ячеек'

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __floordiv__(self, other):
        return Cell(self.cell // other.cell)

    def make_order(self, row):
        i = 0
        new_list = []
        while self.cell >= 0:
            i += 1
            if self.cell - row >= 0:
                new_list.append('*' * row)
            else:
                new_list.append('*' * self.cell)
            self.cell -= row
        return '\n'.join(new_list)


cell_1 = Cell(20)
cell_2 = Cell(13)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_1.make_order(3))
