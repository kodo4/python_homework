class MyOwnErr(Exception):
    def __init__(self, txt=None):
        self.txt = txt

    def is_digit(self, string):
        if string.isdigit():
            return True
        else:
            try:
                float(string)
                return True
            except ValueError:
                return False


a = MyOwnErr()
string = None
my_list = []
while string != 'exit':
    string = input("Enter number. For exit enter 'exit': ")
    try:
        if a.is_digit(string) == False:
            raise MyOwnErr('Это не число')
    except MyOwnErr as err:
        print(err)
    else:
        my_list.append(string)
print(my_list)
