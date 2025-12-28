import re

def translate_word(text):
    vowels = ('a', 'e', 'i', 'o', 'u')
    special_vowels = ('xr', 'yt')
    
    if text.startswith(vowels) or text.startswith(special_vowels):
        return text + 'ay'

    qu_match = re.match(r'^([^aeiou]*qu)(.*)', text)
    if qu_match:
        return qu_match.group(2) + qu_match.group(1) + "ay"

    y_match = re.match(r'^([^aeiou]+)(y.*)', text)
    if y_match:
        return y_match.group(2) + y_match.group(1) + "ay"

    consonant_match = re.match(r'^([^aeiou]+)(.*)', text)
    if consonant_match:
        return consonant_match.group(2) + consonant_match.group(1) + "ay"

    return text + "ay"

def translate(sentence):
    return " ".join(translate_word(word) for word in sentence.split())
