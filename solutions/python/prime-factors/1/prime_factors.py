def factors(value):
    fact = []
    d = 2
    temp = value
    while d * d <= temp:
        while temp % d == 0:
            fact.append(d)
            temp //= d
        d += 1
    if temp > 1:
        fact.append(temp)
    return fact
