import string

def rotate(text, key):
    result = ""
    key = key % 26

    for char in text:
        if char in string.ascii_uppercase:
            new_val = (ord(char) - ord('A') + key) % 26
            result += chr(new_val + ord('A'))
        elif char in string.ascii_lowercase:
            new_val = (ord(char) - ord('a') + key) % 26
            result += chr(new_val + ord('a'))
        else:
            result += char

    return result
