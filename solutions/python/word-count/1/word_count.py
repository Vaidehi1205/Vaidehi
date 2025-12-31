import re

def count_words(sentence):
    words = re.split(r"[^a-z0-9']+", sentence.lower())
    counts = {}

    for word in words:
        if word:
            word = word.strip("'")
            if word:
                counts[word] = counts.get(word, 0) + 1

    return counts
