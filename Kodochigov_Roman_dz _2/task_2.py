input_list = ['в', '5', 'часов', '17', 'минут', 'температура',
              'воздуха', 'была', '+5', 'градусов']
output_list = []
for item in input_list:
    if item.isdigit():
        item = int(item)
        item = f'"{item:02}"'
    if item[0] == "+" or item[0] == "-":
        first = item[0]
        number = int(item[1:])
        item = f'"{first}{number:02}"'
    output_list.append(item)
print(' '.join(output_list))
