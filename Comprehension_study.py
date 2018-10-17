# リスト内包表記のやり方
# 簡単なリストは一行にできる。長いのは向いてない。
t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9)

r = [i for i in t if i % 2 ==0]
print(r)

r = []

for i in t:
    for j in t2:
        r.append(i * j)

print(r)

r = [i * j for i in t for j in t2]

print(r)

# 辞書包括表記のやり方
w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {}
for x, y in zip(w, f):
    d[x] = y

print(d)

# 辞書包括表記
d = {x : y for x, y in zip(w, f)}

print(d)

# 集合内包表記
s = set()

for i in range(10):
    s.add(i)

print(s)

s = {i for i in range(10) if i % 2 == 0}
print(s)

# ジェネレータ内包表記
def g():
    for i in range(10):
        yield i

g = g()
print(type(g))
print(next(g))
print(next(g))
print(next(g))

g = (i for i in range(10))
# タプルの場合 tupleを付ける
# g = tuple(i for i in range(10))

print(next(g))
print(next(g))
print(next(g))
print(next(g))
