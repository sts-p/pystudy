def print_info(func):
    """python Decorator sample.

    Args:
        func (func): set function.
    Returns:
        wrapper: func add 'start' and 'end'.
    """
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

@print_info
def add_num(a, b):
    return a + b

@print_info
@print_more
def sub_num(a, b):
    return a - b

# イチイチ宣言
# f = print_info(add_num)
# r = f(10, 20)
# print(r)
# print(print_info.__doc__)

# r = add_num(10, 20)
# print(r)
r2 = sub_num(10, 20)
# print(r2)