# range関数

# num_list = [0,1,2,3,4,5,6,7,8,9]
# for i in num_list:
#     print(i)

# 連番での処理はrange関数で楽々
for i in range(2, 10, 3):
    print(i)


# "_"(アンダースコア)は使わない
for _ in range(10):
    print('hello')