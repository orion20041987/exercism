# def convert(number):
#     _ = []
#     result = ''
#     if number % 3 == 0:
#         _.append('Pling')
#     if number % 5 == 0:
#         _.append('Plang')
#     if number % 7 == 0:
#         _.append('Plong')
#     for item in _:
#         result += item
#     if result != "":
#         return result
#     else:
#         return str(number)

def convert(number):
    msg = ''.join(drop for divisor, drop in {3: "Pling", 5: "Plang",
                  7: "Plong"}.items() if number % divisor == 0)
    return msg if msg != '' else str(number)

