# enumerate関数使用

# 悪い例
i = 0
for fruit in ['apple', 'banana', 'orange']:
    print(i, fruit)
    i += 1

print('##########################################')

# 良い例 enumerate関数使用例
for j, fruit in enumerate(['apple', 'banana','orange']):
    print(j, fruit)
