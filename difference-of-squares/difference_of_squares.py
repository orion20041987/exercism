def square_of_sum(number):
    sum = 0
    for i in range(1, number + 1):
        sum += i
    square_of_sum_result = sum ** 2
    return square_of_sum_result


def sum_of_squares(number):
    res = 0
    for i in range(1, number + 1):
        res += (i ** 2)
    sum_of_squares_result = res
    return sum_of_squares_result


def difference_of_squares(number):
    sum = 0
    for i in range(1, number + 1):
        sum += i
    square_of_sum_result = sum ** 2
    res = 0
    for i in range(1, number + 1):
        res += (i ** 2)
    sum_of_squares_result = res
    difference_of_squares_result = square_of_sum_result - sum_of_squares_result
    return difference_of_squares_result
