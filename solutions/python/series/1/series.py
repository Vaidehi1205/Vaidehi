def slices(series, length):
    num = list(series)
    com = []
    
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if series == '':
        raise ValueError("series cannot be empty")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    if length == len(series):
        return [series]
    elif length == 1:
        com = num
    else:
        for i in range(len(series) - length + 1):
            com.append(series[i : i + length])


    return com

    


