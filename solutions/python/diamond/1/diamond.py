def rows(letter):
    n = ord(letter) - ord('A')
    width = 2 * n + 1
    result = []

    for i in range(n + 1):
        ch = chr(ord('A') + i)
        if i == 0:
            row = ch
        else:
            row = ch + " " * (2 * i - 1) + ch

        result.append(row.center(width))

    for i in range(n - 1, -1, -1):
        result.append(result[i])

    return result
