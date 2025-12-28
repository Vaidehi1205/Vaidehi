"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 0

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    
    if is_contiguous_subsequence(list_one, list_two):
        return SUBLIST
        
    if is_contiguous_subsequence(list_two, list_one):
        return SUPERLIST
        
    return UNEQUAL

def is_contiguous_subsequence(smaller, larger):
    if not smaller:
        return True
    
    len_s, len_l = len(smaller), len(larger)
    
    for i in range(len_l - len_s + 1):
        if larger[i : i + len_s] == smaller:
            return True
            
    return False
