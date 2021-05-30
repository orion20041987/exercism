import re


def is_isogram(string):
    letter_list = re.findall(r'\w+', string)
    res = []
    for item in letter_list:
        res += item
    print(res)
    for item in res:
        print(res.count(item))


print(is_isogram('abc'))
