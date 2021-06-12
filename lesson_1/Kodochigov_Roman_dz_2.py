start_list = []
total_1 = 0
total_2 = 0

for i in range(1, 1000, 2):
    number = i ** 3
    start_list.append(number)

for i in start_list:
    count = 0
    for number in str(i):
        count += int(number)
    if not count % 7:
        total_1 += i

for i in start_list:
    i += 17
    count = 0
    for number in str(i):
        count += int(number)
    if not count % 7:
        total_2 += i

print(total_1)
print(total_2)
