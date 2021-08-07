def largest(min_factor, max_factor):
    number_list = list(get_range_and_factors(min_factor, max_factor))
    value = max_palindrome(number_list)
    m_factor = max_factor
    factors = factors_define(value, m_factor)
    print(value, factors)
    return value, factors


def smallest(min_factor, max_factor):
    pass


def get_range_and_factors(min_factor, max_factor):
    numb = []
    res_list = []
    for item in range(min_factor, max_factor + 1):
        numb.append(item)
        res_list.append(item)
    while len(numb) > 1:

        a = numb.pop(0)
        for item in numb:
            b = (a * item)
            res_list.append(b)
    return set(res_list)


def max_palindrome(number_list):
    potencial_palindrome_list = []
    for item in sorted(number_list):
        potencial_palindrome_list.append(item)
    for index in range(-1, -(len(potencial_palindrome_list)) - 1, -1):
        if str(potencial_palindrome_list[index]) == (str(potencial_palindrome_list[index])[::-1]):
            return potencial_palindrome_list[index]


def factors_define(value, m_factor):
    factor_list = []
    for factor in range(1, round((value / 2)) + 1):
        if value % factor == 0 and factor < m_factor and int(value / factor) <= m_factor:
            factor_list.append([factor, int(value / factor)])
    return factor_list


largest(100, 999)
