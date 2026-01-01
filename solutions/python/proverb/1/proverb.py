def proverb(*input_data, qualifier):
    words = list(input_data)

    res = []

    if words == []:
        return words
    if len(words) == 1:
        if qualifier == None:
                    res.append('And all for the want of a '                                  +words[0]+'.')
        else:
                    res.append('And all for the want of a '                                 +qualifier+' '+words[0]+'.')


    else:
        for i in range(len(words)):
            if i != (len(words)-1):
                res.append('For want of a ' +words[i]+ ' the '                             +words[i+1]+ ' was lost.')
            else:
                if qualifier == None:
                            res.append('And all for the want of a '                                  +words[0]+'.')
                else:
                            res.append('And all for the want of a '                                 +qualifier+' '+words[0]+'.')
                    
    return res
        
    
        
