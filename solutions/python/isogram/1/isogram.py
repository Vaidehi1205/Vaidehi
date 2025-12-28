import string

def is_isogram(strings):
    lowered_string = strings.lower()
    
    alphabetic_chars = [char for char in lowered_string if char.isalpha()]

    total_chars_count = len(alphabetic_chars)

    unique_chars_count = len(set(alphabetic_chars))
    
    return total_chars_count == unique_chars_count
