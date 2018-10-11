print('''
# ディクショナリのコピー メソッドによるもの
 ''')
x = {'a' : 1}
y = x['a'] = 100
print(x)
print(y)

x = {'a':1}

# listのコピーと同様にcopy()メソッドを使用
y = x.copy()
y['a'] = 1000

print(x)
print(y)

print('''
# 用途 keyがわかっているならdictionaryが有効。ハッシュテーブルで検索するのでlistより早い
 ''')
fruits = {
    'apple': 100,
    'banana': 200,
    'orange': 300,
 }

print(fruits['apple'])
