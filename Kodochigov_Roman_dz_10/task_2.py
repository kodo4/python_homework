from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def fab_cons(self):
        pass

    def __add__(self, other):
        return f'Общий метраж: {self.fab_cons + other.fab_cons}м'


class Coat(Clothes):
    @property
    def fab_cons(self):
        cons = round(self.param / 6.5) + 0.5
        return cons


class Suit(Clothes):
    @property
    def fab_cons(self):
        cons = round((2 * self.param + 0.3) / 100)
        return cons


coat = Coat(42)
suit = Suit(170)
print(coat.fab_cons)
print(suit.fab_cons)
print(coat + suit)
