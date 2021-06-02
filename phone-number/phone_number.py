import re


class PhoneNumber:
    def __init__(self, num):
        self.num = num




    def number(self):
        parsed_num = [digit for digit in self.num if digit.isdigit()]
        if len(parsed_num) < 10 or len(parsed_num) > 11:
            # print('_______ValueError(Cell number must be 10 or 11 digits long)\n')
            raise ValueError('Cell number must be 10 or 11 digits long')
        elif len(parsed_num) == 11 and parsed_num[0] != "1":
            # print('_______ValueError(Country code must be equal "1")\n')
            raise ValueError('Country code must be equal "1"')
        elif len(parsed_num) == 10:
            # print(f'Original number: {parsed_num}')
            parsed_num.insert(0, '1')
            # print(f'Added country code {parsed_num}')
        else:
            pass
            # print(f'Cell number is valid: {parsed_num}')

        if int(parsed_num[1]) < 2 or int(parsed_num[4]) < 2:
            # print('_______ValueError(Wrong cell number format (NXX)-NXX-XXXX))\n')
            raise ValueError('Wrong cell number format (NXX)-NXX-XXXX))')
        elif len(parsed_num) == 11:
            cell_number = ''.join(parsed_num[1:])
            # print(f'Result number is: {cell_number}\n')
            return cell_number

    def pretty(self):
        pass


if __name__ == "__main__":
    number = PhoneNumber("1(223) 456-7890").number()
    number = PhoneNumber("123456789").number()
    number = PhoneNumber("(223) 456-7890").number()
    number = PhoneNumber("1223456789").number()
    number = PhoneNumber("(223) 456-7890").number()
    number = PhoneNumber("(223) 456-7890").number()
    number = PhoneNumber("(223) 456-7890").number()
    number = PhoneNumber("(223) 456-7890").number()
    number = PhoneNumber('+1 (111) 111-1111').number()
    number = PhoneNumber('21234567890').number()
    number = PhoneNumber('22234567890').number()
