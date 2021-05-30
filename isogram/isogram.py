import re


def is_isogram(string):
    letter_list = re.findall(r'\w+', string)
    res = []
    for item in letter_list:
        res += item
    # print(res)
    # for item in res:
    #     print(res.count(item))

    print([[item, res.count(item)] for item in set(res)])
    tmp = [[item, res.count(item)] for item in set(res)]
    for a in tmp:
        if a[1] != 1:
            return False
        return True




print(is_isogram('adfkgrkjrengkejfopwnfbc'))
print(is_isogram('adcdrfvtgbyhnmju'))
