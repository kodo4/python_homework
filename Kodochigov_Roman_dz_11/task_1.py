class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def splitting(cls, date):
        d, m, y = date.split('-')
        d, m, y = int(d), int(m), int(y)
        return d, m, y

    @staticmethod
    def validation(date):
        d, m, y = Date.splitting(date)
        try:
            if 0 < d < 32:
                print(f'day {d} - OK')
            else:
                raise ValueError
        except ValueError:
            print("День несоответствующее значение")

        try:
            if 0 < m < 13:
                print(f'month {m} - OK')
            else:
                raise ValueError
        except ValueError:
            print("Месяц несоответствующее значение")

        try:
            if 1900 < y < 2022:
                print(f'year {y} - OK')
            else:
                raise ValueError
        except ValueError:
            print("Год несоответствующее значение")


date = input('Enter date in format "dd-mm-yyyy: ')
Date.splitting(date)
Date.validation(date)
