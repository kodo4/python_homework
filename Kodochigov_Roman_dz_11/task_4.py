class Warehouse:
    warehouse = {'printers': {'laser': 1,
                              'inky': 2},
                 'scanners': {'3D': 2,
                              'barcode': 3},
                 'xerox': {'analog': 0,
                           'digital': 1,
                           'color': 2}}

    def __str__(self):
        return f'{self.warehouse}'

    def add(self, name, type):
        self.warehouse[name][type] += 1

    def delete(self, name, type):
        self.warehouse[name][type] -= 1


class OfficeEquipment:
    def __init__(self, name):
        self.name = name


class Printer(OfficeEquipment):
    def __init__(self, name, type, company):
        super().__init__(name)
        self.type = type
        self.company = company


class Scanner(OfficeEquipment):
    def __init__(self, name, type, company):
        super().__init__(name)
        self.type = type
        self.company = company


class Xerox(OfficeEquipment):
    def __init__(self, name, type, company):
        super().__init__(name)
        self.type = type
        self.company = company


a = Warehouse()
action = None
while action != 'exit':
    action = input('1 - добавить на склад, 2 - списать со склада, 3 - показать склад. For exit enter "exit": ')
    if action == '1':
        action = input('1 - printer, 2 - scanner, 3 - xerox ')
        if action == '1':
            action = input('1 - laser, 2 - inky ')
            if action == '1':
                a.add('printers', 'laser')
            elif action == '2':
                a.add('printers', 'inky')
        elif action == '2':
            action = input('1 - 3D, 2 - barcode ')
            if action == '1':
                a.add('scanners', '3D')
            elif action == '2':
                a.add('scanners', 'barcode')
        elif action == '3':
            action = input('1 - analog, 2 - digital, 3 - color')
            if action == '1':
                a.add('xerox', 'analog')
            elif action == '2':
                a.add('xerox', 'digital')
            elif action == '3':
                a.add('xerox', 'color')
    elif action == '2':
        action = input('1 - printer, 2 - scanner, 3 - xerox ')
        if action == '1':
            action = input('1 - laser, 2 - inky ')
            if action == '1':
                a.delete('printers', 'laser')
            elif action == '2':
                a.delete('printers', 'inky')
        elif action == '2':
            action = input('1 - 3D, 2 - barcode ')
            if action == '1':
                a.delete('scanners', '3D')
            elif action == '2':
                a.delete('scanners', 'barcode')
        elif action == '3':
            action = input('1 - analog, 2 - digital, 3 - color')
            if action == '1':
                a.delete('xerox', 'analog')
            elif action == '2':
                a.delete('xerox', 'digital')
            elif action == '3':
                a.delete('xerox', 'color')
    elif action == '3':
        print(a)
