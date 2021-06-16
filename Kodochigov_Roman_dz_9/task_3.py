class Worker:
    def __init__(self, n, s, p, wage, bonus):
        self.name = n
        self.surname = s
        self.position = p
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        full_name = f'{self.surname} {self.name}'
        return full_name

    def get_total_income(self):
        money = 0
        for value in self._income.values():
            money += value
        return money


a = Position('Roman', 'Kodochigov', 'IO', 20000, 3000)
print(a.name)
print(a.surname)
print(a.position)
print(a._income)
print(a.get_full_name())
print(a.get_total_income())
