translate = {'one': 'один', 'two': 'два', 'three': 'три',
             'four': 'четыре', 'five': 'пять', 'six': 'шесть',
             'seven': 'семь', 'eight': 'восемь', 'nine': 'девять',
             'ten': 'десять'}


def num_translate_adv(num):
    if num.istitle():
        num = num.lower()
        translate_word = translate.get(num)
        print(translate_word.capitalize())
    else:
        print(translate.get(num))


number = input("Enter number: ")
num_translate_adv(number)
