def say(number):
    if not 0 <= number <= 999_999_999_999:
        raise ValueError("input out of range")
    
    if number == 0:
        return "zero"

    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", 
             "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    scales = ["", "thousand", "million", "billion"]

    def chunk_to_words(n):
        parts = []
        if n >= 100:
            parts.append(units[n // 100] + " hundred")
            n %= 100
        if n >= 20:
            word = tens[n // 10]
            if n % 10:
                word += "-" + units[n % 10]
            parts.append(word)
        elif n > 0:
            parts.append(units[n])
        return " ".join(parts)

    res = []
    for i, scale in enumerate(scales):
        number, chunk = divmod(number, 1000)
        if chunk > 0:
            chunk_words = chunk_to_words(chunk)
            if scale:
                chunk_words += " " + scale
            res.append(chunk_words)

    return " ".join(reversed(res)).strip()
