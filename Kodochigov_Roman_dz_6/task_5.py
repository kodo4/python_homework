from sys import argv
program, *args = argv
with open(args[0], encoding='utf-8') as a, \
        open(args[1], encoding='utf-8') as b, \
        open(args[2], 'w', encoding='utf-8') as c:
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
