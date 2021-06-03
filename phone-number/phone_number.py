class PhoneNumber:
    def __init__(self, num):
        self.num = num
        parsed_num = [digit for digit in self.num if digit.isdigit()]
        if len(parsed_num) < 10 or len(parsed_num) > 11:
            raise ValueError('Cell number must be 10 or 11 digits long')
        elif len(parsed_num) == 11 and parsed_num[0] != "1":
            raise ValueError('Country code must be equal "1"')
        elif len(parsed_num) == 10:
            parsed_num.insert(0, '1')
        else:
            pass

        if int(parsed_num[1]) < 2 or int(parsed_num[4]) < 2:
            raise ValueError('Wrong cell number format (NXX)-NXX-XXXX))')
        elif len(parsed_num) == 11:
            cell_number = ''.join(parsed_num[1:])
            area_code = ''.join(parsed_num[1:4])
            pretty_number = '(' + ''.join(parsed_num[1:4]) + ')' + '-' + ''.join(parsed_num[4:7]) + '-' + ''.join(
                parsed_num[7:11])
            self.number = cell_number
            self.area_code = area_code
            self.pretty_number = pretty_number

    def number(self):
        return self.number

    def pretty(self):
        return self.pretty_number
