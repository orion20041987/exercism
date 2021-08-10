def square(number):
    if 0 >= number or number > 64:
        raise ValueError('ValueError')
    if number <= 2:
        return number
    else:
        result = pow(2, number - 1)
        return result


def total():
    result = 0
    for item in range(1, 65):
        result += square(item)
    return result


print([x for x in range(64)])
