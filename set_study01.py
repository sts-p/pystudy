"""
集合
a = (値1, 値2, 値3...) ex. a = (1,2,3,3,2,4,4)
"""
# 使い道
print('# 集合の使い道 共通の友人')
my_friends = {'A', 'C', 'D'}
A_friends = {'B', 'D', 'E', 'F'}

print(my_friends & A_friends)


# 型変換
print('# 型変換')
fruits = ['apple', 'banana', 'apple', 'banana']
kind = set(fruits)
print(kind)

