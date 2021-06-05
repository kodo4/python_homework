input_list = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34,
              98.90, 70.01, 63, 39, 90.47, 29, 24, 42, 59.11,
              45.78, 48.29, 8.53, 67, 95, 5.62, 11, 18.34, 13,
              64.80, 78, 93, 88.08]
# Вывести цены в одну строку с форматирование примера "1 руб 08 коп"
output_list = []
for item in input_list:
    rub = int(item)
    kop = int(item * 100 % 100)
    text = f'{rub} руб {kop:02} коп'
    output_list.append(text)
print(', '.join(output_list))
# Отсортировать список по возрастанию и доказать что in_place
print(input_list)
print(id(input_list))
input_list.sort()
print(input_list)
print(id(input_list))

# Создать новый список, но цены по убыванию
output_reversed = sorted(input_list, reverse = True)
print(output_reversed)
print(id(output_reversed))

# вывести цены пяти самых дорогих по возрастанию
print(input_list[-5:])
