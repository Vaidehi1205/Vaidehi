def find_anagrams(word, candidates):
    word_sorted = sorted(word.lower())
    result = []

    for c in candidates:
        if c.lower() != word.lower() and sorted(c.lower()) == word_sorted:
            result.append(c)

    return result
