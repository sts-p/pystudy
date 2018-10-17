l = ['Good morning', 'Good afternoon', 'Good night']

for i in l:
    print(i)

print('####################################')

def greeting():
    """yieldを使用したジェネレータ。
    Args:
        None.
    return:
        None.

    """
    yield 'Good mornig'
    yield 'Good afternoon'
    yield 'Good night'

g = greeting()
print(next(g))
print(next(g))
print(next(g))

print('######################################')
def counter(num=10):
    for _ in range(num):
        yield 'run'

c = counter()
print(next(c))
