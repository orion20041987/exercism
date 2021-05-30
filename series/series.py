def slices(series, length):
    if length > len(series) or length <= 0 or series == '':
        raise ValueError('wrong input data')

    start = 0
    result = []
    while start + length < len(series) + 1:
        result.append(series[start:start+length])
        start += 1
    return [item for item in result]



