def square_of_sum(number):
    for i in range(number):
        sum += i
    square_of_sum_result = sum ** 2
    return square_of_sum_result


def sum_of_squares(number):
    for i in range(number):
        res = 0
        res += (i ** 2)
    sum_of_squares_result = res
    return sum_of_squares_result


def difference_of_squares(number):
    difference_of_squares_result = square_of_sum_result - sum_of_squares_result
