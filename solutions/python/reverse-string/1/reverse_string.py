def reverse(text):

    sp = list(text)
    
    if text == "":
        return text
    else:
        sp.reverse()
        r = ''.join(sp)
        return r


        
