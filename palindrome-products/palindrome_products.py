def largest(min_factor, max_factor):
    if min_factor > max_factor:
        value = None
        factors = []
        raise ValueError('min_factor is largest than max_factor')
    number_list = list(get_range_and_factors(min_factor, max_factor))
    value = max_palindrome(number_list)
    max_factor = max_factor
    factors = factors_define(value, max_factor=max_factor)
    return value, factors


def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        value = None
        factors = []
        raise ValueError('min_factor is largest than max_factor')
    number_list = list(get_range_and_factors(min_factor, max_factor))
    value = min_palindrome(number_list)
    min_factor = min_factor
    factors = factors_define(value, min_factor=min_factor)
    return value, factors


def get_range_and_factors(min_factor, max_factor):
    numb = []
    res_list = []
    for item in range(min_factor, max_factor + 1):
        numb.append(item)
        # res_list.append(item)
    while len(numb) > 1:

        a = numb[0]
        for item in numb:
            b = (a * item)
            res_list.append(b)
        numb.pop(0)
    # print(set(res_list))
    return set(res_list)


def max_palindrome(number_list):
    potencial_palindrome_list = []
    for item in sorted(number_list):
        potencial_palindrome_list.append(item)
    for index in range(-1, -(len(potencial_palindrome_list)) - 1, -1):
        try:
            if str(potencial_palindrome_list[index]) == (str(potencial_palindrome_list[index])[::-1]):
                return potencial_palindrome_list[index]
        except IndexError:
            return None


def min_palindrome(number_list):
    potencial_palindrome_list = []
    for item in sorted(number_list):
        potencial_palindrome_list.append(item)
    for index in range(0, len(potencial_palindrome_list) + 1):
        try:
            if str(potencial_palindrome_list[index]) == (str(potencial_palindrome_list[index])[::-1]):
                return potencial_palindrome_list[index]
        except IndexError:
            return None


def factors_define(value, max_factor=0, min_factor=0):
    if min_factor == 0:
        factor_list = []
        if value == None:
            return factor_list
        for factor in range(1, (round((value / 2)) + 1) + 1):
            if value % factor == 0 and factor <= max_factor and int(value / factor) <= max_factor:
                try:
                    if factor_list[-1][1] != factor:
                        factor_list.append([factor, int(value / factor)])
                except IndexError:
                    factor_list.append([factor, int(value / factor)])
        return factor_list
    if max_factor == 0:
        factor_list = []
        if value == None:
            return factor_list
        for factor in range(min_factor, (round((value / 2)) + 1) + 1):
            if value % factor == 0 and factor >= min_factor and int(value / factor) >= min_factor:
                try:
                    if factor_list[-1][1] != factor:
                        factor_list.append([factor, int(value / factor)])
                except IndexError:
                    factor_list.append([factor, int(value / factor)])
        return factor_list
