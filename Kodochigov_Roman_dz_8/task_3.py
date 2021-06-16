def type_logger(func):
    def wrapper(*args):
        result = [*args]
        for i in result:
            print(f'{func.__name__}({i}: {type(i)}', end=', ')
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5, 4)
