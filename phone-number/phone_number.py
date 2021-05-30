import re


class PhoneNumber:
    def __init__(self, num):
        self.num = re.findall(r'\d+', num)
        res = ''
        for item in self.num:
            res += item
        if len(res) == 10 and re.findall(r'[2-9]{1}[0-9]{2}[2-9]{1}[0-9]{6}', res):
            res = '1' + res
            print(f'add 1 at number. result is: {res}')
        else:
            print(f'Единицу не добавляем {res}')
        if not re.findall(r'[1]{1}[2-9]{1}[0-9]{2}[2-9]{1}[0-9]{6}', res):
            print('Value error')
        else:
            self.res = res



    def number(self):
        res = self.res
        print(f'qqq {res[0:10]}')
        return res[0:10]

    def pretty(self):
        pass


if __name__ == "__main__":
    # number = PhoneNumber("1(223) 456-7890").number()
    # number = PhoneNumber("123456789").number()
    # number = PhoneNumber("(223) 456-7890").number()
    # number = PhoneNumber("1223456789").number()
    # number = PhoneNumber("(223) 456-7890").number()
    # number = PhoneNumber("(223) 456-7890").number()
    # number = PhoneNumber("(223) 456-7890").number()
    # number = PhoneNumber("(223) 456-7890").pretty()
    # number = PhoneNumber('+1 (111) 111-1111').pretty()
    # number = PhoneNumber('21234567890').pretty()
    # PhoneNumber("22234567890")
