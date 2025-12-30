import re


def decode(string):
    res = ""
    count_str = ""
    
    for char in string:
        if char.isdigit():
            count_str += char
        else:
            count = int(count_str) if count_str else 1
            res += char * count
            count_str = "" 

    return res

def encode(string):
    if not string:
        return ""
    
    res = ''
    count = 1 
    
    for i in range(len(string)):
        if i + 1 < len(string) and string[i] == string[i+1]:
            count += 1
        else:
            if count > 1:
                res += str(count) + string[i]
            else:
                res += string[i]
            
            count = 1
            
    return res


