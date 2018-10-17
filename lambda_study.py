# lambdaを使わない例
l = ['Mon', 'tue', 'Wed', 'Thu', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

def sample_func(word):
    return word.capitalize()

change_words(l, sample_func)

print('#####################################')

# lambdaを使った例

change_words(l, lambda word: word.capitalize())
print('#####################################')
change_words(l, lambda word: word.lower())
