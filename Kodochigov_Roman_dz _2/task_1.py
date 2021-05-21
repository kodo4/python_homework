expressions = [15 * 3, 15 / 3, 15 // 2, 15 ** 2]

for ind in range(len(expressions)):
    print(f'{expressions[ind]:<3} - {type(expressions[ind])}')