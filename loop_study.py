'''
ループ処理のあれこれ
'''

# while
# count = 0
# while count < 5:
#     if count == 1:
#         break
#         # continueもjavaと同様に使用可
#     print(count)
#     count += 1
# else:
#     # 最後までループが回ったときのみ実行
#     print('done')

# input関数
# while True:
#     word = input('Enter:')
#     num = int(word)
#     if num == 100:
#         break
#     print('next')


# for文(イテレータ)　配列
# some_list = [1,2,3,4,5]

# for i in some_list:
#     print(i)

# # 文字列でも可能
# for s in 'abcde':
#     print(s)

# elseもwhile elseと同様
for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'banana':
        print('stop eating')
        break
    print(fruit)
else:
    print('I ate all!')