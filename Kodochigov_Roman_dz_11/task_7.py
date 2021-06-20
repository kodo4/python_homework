class ComplexNumber:
    def __init__(self, z1):
        self.z1 = z1

    def __add__(self, other):
        a1, c1 = self.z1.split('+')
        a2, c2 = other.z1.split('+')
        b1 = c1[1:]
        b2 = c2[1:]
        return f'({int(a1) + int(a2)} + i{int(b1) + int(b2)})'

    def __mul__(self, other):
        a1, c1 = self.z1.split('+')
        a2, c2 = other.z1.split('+')
        b1 = c1[1:]
        b2 = c2[1:]
        return f'({(int(a1) * int(a2) - int(b1) * int(b2))} + i{(int(a1) * int(b2) + int(a2) * int(b1))})'


s = ComplexNumber('5+i4')
t = ComplexNumber('10+i5')
print(s+t)
print((5+4j) + (10 + 5j))
print(s*t)
print((5+4j) * (10 + 5j))
