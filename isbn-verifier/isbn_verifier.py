def is_valid(isbn):
    if isbn == '': return False
    parsed_number = [digit for digit in isbn if digit.isdigit()]
    if isbn[-1] == 'X': parsed_number.append('10')
    if len(parsed_number) != 10: return False
    valid_sum = 0
    factor = len(parsed_number)
    for i in range(0, len(parsed_number)):
        valid_sum += int(parsed_number[i]) * (factor - i)
    if valid_sum % 11 == 0:
        return True
    else:
        return False

