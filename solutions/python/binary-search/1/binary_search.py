def find(search_list, value):

    n = int(len(search_list)/2)
    left_list = search_list[:n]
    right_list = search_list[n:]

    if value not in search_list:
        raise ValueError("value not in array")

    
    if value == search_list[n]:
        return n
    elif value < search_list[n] :
        for i in range(len(left_list)):
            if value == left_list[i]:
                return search_list.index(value)
    elif value > search_list[n] :
        for i in range(len(right_list)):
            if value == right_list[i]:
                return search_list.index(value)
    
        
        
