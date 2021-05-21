input_list = ['инженер-конструктор Игорь',
              'главный бухгалтер МАРИНА',
              'токарь высшего разряда нИКОЛАй',
              'директор аэлита']

for item in input_list:
    new_str = item.split()
    name = new_str[-1]
    print(f'Привет, {name.title()}!')