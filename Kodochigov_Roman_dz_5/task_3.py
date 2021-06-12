from itertools import zip_longest
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Борис', 'Елена',
    'Иван', 'Анастасия',
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

tup = zip_longest(tutors, klasses, fillvalue=None)
for i in range(len(tutors)):
    print(next(tup))
