# zip関数使用
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

# 悪い例　使わない
for i in range(len(days)):
    print(days[i], fruits[i], drinks[i])

print('#############################################')

# 良い例 zip関数使用 インデックスをイチイチ使用しなくていい！
for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)
