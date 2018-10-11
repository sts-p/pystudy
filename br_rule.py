"""
改行
80文字以上のコードは改行する。
"""
# backslashによるコードの改行
s = 'aaaaaaaaaaaaa' \
 + 'bbbbbbbbbbbb'

print(s)

# 数値にも適用可能
x = 1 + 1 + 1 + 1 + 1 \
  + 1 + 1 + 1

print(x)


# "()"parenthesisでもOK

y = ('xxxxxxxxxxxxxxxxx'
 'yyyyyyyyyyyyyyyyyyyy')

print(y)
