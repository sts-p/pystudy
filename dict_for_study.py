d = {'x': 100, 'y': 200}

# itemsメソッドはタプル型でリストを返す
print(d.items())

# for文の時はタプルをアンパッキングした値で返す
for k, v in d.items():
    print(k, ':', v)
