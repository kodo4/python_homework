translate = {'one': 'один', 'two': 'два', 'three': 'три',
             'four': 'четыре', 'five': 'пять', 'six': 'шесть',
             'seven': 'семь', 'eight': 'восемь', 'nine': 'девять',
             'ten': 'десять'}


def num_translate(num):
    print(translate.get(num))


number = input("Enter number: ")
num_translate(number)
