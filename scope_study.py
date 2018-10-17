# グローバルな変数として扱われる
animal = 'cat'

def f():
    # animal = 'dog'
    print('local:', locals())



f()
print('global:', animal)
print('global2:', globals())