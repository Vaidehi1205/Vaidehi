import re

def abbreviate(words):
    clean_words = words.replace("'", "").replace("_", " ").replace("-", " ")
    
    acr = "".join(word[0] for word in clean_words.split())
    
    return acr.upper()
