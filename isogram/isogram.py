import re


def is_isogram(string):
    if string == '':
        return True
    parsed_string = re.findall(r'\w+', string.lower())
    # string = re.sub(r"\W", "", string).lower()  \\заменит любой элемент строки на параметр, если он не
    #                                             \\удовлетворяет паттерну
    letter_list = []
    for item in parsed_string:
        letter_list += item
    counter = [[item, letter_list.count(item)] for item in set(letter_list)]
    for a in counter:
        if a[1] != 1:
            return False
    return True

