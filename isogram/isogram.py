import re


def is_isogram(string):
    if string == '':
        return True
    letter_list = re.findall(r'\w+', string.lower())
    res = []
    for item in letter_list:
        res += item

    tmp = [[item, res.count(item)] for item in set(res)]
    for a in tmp:
        if a[1] != 1:
            return False
    return True

