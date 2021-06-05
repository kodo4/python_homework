from sys import argv

program, *args = argv
result = args

if not result:
    with open('sales.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line.replace('\n', ''))
elif len(result) == 1:
    with open('sales.txt', 'r', encoding='utf-8') as f:
        content = [line.replace('\n', '') for line in f]
        for i in range(int(result[0])-1, len(content)):
            print(content[i])
elif len(result) == 2:
    with open('sales.txt', 'r', encoding='utf-8') as f:
        content = [line.replace('\n', '') for line in f]
        for i in range(int(result[0])-1, int(result[1])):
            print(content[i])
