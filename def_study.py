# 関数作成

def say_anything():
    print('hi')

# 関数定義をしてから関数を呼び出す
say_anything()
print(say_anything)

print('##################################')

# 返り値あり
def say_anything2():
    r = 'hi hi'
    return r

print(say_anything2())

print('##################################')

# 引数&返り値
# 引数は(a: int, b: int)というように型の宣言ができるが、文字列型も入れれるので、宣言しなくても良い
def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"

result = what_is_this('red')
print(result)
result = what_is_this('green')
print(result)
result = what_is_this('yellow')
print(result)

print('##################################')

# 位置引数、キーワード引数
def menu(entree, drink, dessert):
    print(entree)
    print(drink)
    print(dessert)

# よくあるやつ(位置引数)
menu('chikin', 'milk', 'fruit')

# キーワードアーギュメント(キーワード引数)
menu(drink='beer', dessert='ice', entree='beef')

print('##################################')

# デフォルト引数
# 
# デフォルト引数での注意点
# リスト型を引数として"l=[]"というようにやってしまうと、参照渡しで動作するため、
# リストの値が増え続けてしまうので、バグにつながることが多い。
# そういう場合は、"l=None"として以下の通りにする
# def listFunc(x, l=None):
#     if l is None:
#         l = []
#     l.append(x)
#     return l
# 
# 空のリストやディクショナリを引数にする場合は十分に注意すること。
# ※Noneはオブジェクトとなるため、isで比較する

def menu2(entree='takoyaki', drink='coke', dessert='mochi'):
    print(entree)
    print(drink)
    print(dessert)

# デフォルト
menu2()

# 引数の入れ替え、デフォルトのままも使用可能
menu2(dessert='ice', entree='beef')

print('##################################')

# 位置引数のタプル化
def say_something(word, *args):
    print("word =", word)
    for arg in args:
        print(arg)

# タプル化 複数の引数をまとめられる
say_something('Hi', 'Mike', 'Nance')

# タプルでも可能 あまり使われない
t = ('Jhon', 'Elie')
say_something('Hello', *t)


