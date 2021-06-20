with open('users.csv', encoding='utf-8') as a, \
        open('hobby.csv', encoding='utf-8') as b, \
        open('users_hobby.txt', 'w', encoding='utf-8') as c:
    for line in a:
        name = line.replace('\n', '')
        hobby = b.readline().replace('\n', '')
        if hobby == '':
            txt = f'{name}: None\n'
        elif name == '':
            exit(1)
        else:
            txt = f'{name}: {hobby}\n'
        c.write(txt)
