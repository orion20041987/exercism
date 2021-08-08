def steps(number):
    if number <= 0:
        raise ValueError('number must be greater than zero')
    step_counter = 0
    while number != 1:
        if number % 2 == 0:
            number = if_even(number, step_counter)
            step_counter += 1
        elif number % 2 == 1:
            number = if_odd(number, step_counter)
            step_counter += 1

    return step_counter


def if_even(number, step_counter):
    number = number / 2
    return int(number)


def if_odd(number, step_counter):
    number = number * 3 + 1
    return int(number)
