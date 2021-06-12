import re
RE_CUBE = re.compile('[^-]')
def val_checker(x):
    def _val_checker(func):
        def wrapper(*args):
            result = func(*args)
            if RE_CUBE.match(str(result)):
                return result
            else:
                raise ValueError(f'wrong val {args[0]}')
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cub(x):
    return x ** 3


print(calc_cub(-5))
