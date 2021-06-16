my_dict = {}
with open('test.txt', encoding='utf-8') as a, open('hobby.csv', encoding='utf-8') as b:
    for line in a:
        name = line.replace('\n', '')
        hobby = b.readline().replace('\n', '')
        if hobby == '':
            my_dict[name] = None
        elif name == '':
            exit(1)
        else:
            my_dict[name] = hobby
print(my_dict)
