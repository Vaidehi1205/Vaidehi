def is_valid(isbn):
    isbn_clean = isbn.replace('-', '').upper()

    if len(isbn_clean) != 10:
        return False

    checksum = 0
    for i, char in enumerate(isbn_clean):
        if i == 9 and char == 'X':
            digit_value = 10
        elif char.isdigit():
            digit_value = int(char)
        else:
            return False
        
        weight = 10 - i
        checksum += digit_value * weight

    return checksum % 11 == 0
