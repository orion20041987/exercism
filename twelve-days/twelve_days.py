def recite(start_verse, end_verse):
    if start_verse < 0 or end_verse > 12 or start_verse > end_verse:
        raise ValueError('Incorrect input indexes')

    output_data = []
    for n in range(start_verse, end_verse + 1):
        days_list = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth',
                     'eleventh', 'twelfth']
        gifts_list = ['a Partridge in a Pear Tree', 'two Turtle Doves', 'three French Hens', 'four Calling Birds',
                      'five Gold Rings', 'six Geese-a-Laying', 'seven Swans-a-Swimming', 'eight Maids-a-Milking',
                      'nine Ladies Dancing', 'ten Lords-a-Leaping', 'eleven Pipers Piping', 'twelve Drummers Drumming']
        separator = ', '
        gifts_list_slice = gifts_list[n - 1: 0: -1]
        if n == 1:
            variable_text = gifts_list[n - 1]
        else:
            variable_text = separator.join(gifts_list_slice) + f', and {gifts_list[0]}'

        output_text = f'On the {days_list[n - 1]} day of Christmas my true love gave to me: {variable_text}.'
        output_data.append(output_text)
    return output_data
