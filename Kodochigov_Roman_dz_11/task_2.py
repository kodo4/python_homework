class MyOwnErr(Exception):
    def __init__(self, txt):
        self.txt = txt


a = int(input('Введите делитель числу 10: '))

try:
    if a == 0:
        raise MyOwnErr('Делить на ноль нельзя!!!')
except MyOwnErr as err:
    print(err)
else:
    print(f'{a} - на это число можно разделить')
    print(10 / a)
