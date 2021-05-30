def classify(number):
    divisor_list = []
    if number <= 0:
        raise ValueError(".+")
    for divisor in range(1, number // 2 + 1):
        if number % divisor == 0:
            divisor_list.append(divisor)

    aliquot_sum = 0
    for elem in divisor_list:
        aliquot_sum += elem
    if aliquot_sum == number:
        return 'perfect'
    elif aliquot_sum < number:
        return 'deficient'
    elif aliquot_sum > number:
        return 'abundant'
