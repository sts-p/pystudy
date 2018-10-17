# l = [1, 2, 3]
# i = 5
# # del l

# try:
#     l[0]
# except IndexError as ex:
#     print("Don't worr: {}".format(ex))
# except NameError as ex:
#     print(ex)
# except Exception as ex:
#     print('other:{}'.format(ex))
# else:
#     print('done')
# finally:
#     print('clean up')

# 独自例外
class UppercaseError(Exception):
    pass

def check():
    words = ['APPLE', 'banana', 'orange']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)
try:
    check()
except UppercaseError as ex:
    print('This is my fault. Go next')