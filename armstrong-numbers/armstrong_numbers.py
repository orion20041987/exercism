def is_armstrong_number(number):
    result = 0
    for x in list(str(number)):
        result += pow(int(x), len(str(number)))
    return number == result

