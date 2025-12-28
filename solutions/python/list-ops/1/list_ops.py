def append(list1, list2):
    return list1 + list2

def concat(lists):
    return [item for sublist in lists for item in sublist]

def filter(function, list):
    re =[]
    for i in range(len(list)):
        if list[i] % 2 == 1:
            re.append(list[i])

    return re

def length(list):
    return len(list)


def map(function, list):
    result_list = []
    for item in list:
        processed_item = function(item)
        result_list.append(processed_item)
    return result_list

def foldl(function, list, initial):
    accumulator = initial
    
    for item in list:
        accumulator = function(accumulator, item)
        
    return accumulator


def foldr(function, list, initial):
    accumulator = initial
    
    for item in reversed(list):
        accumulator = function(accumulator,item)
        
    return accumulator


def reverse(list):
    rev = []
    if list == []:
        return list
    else:
        for i in reversed(list):
            rev.append(i)

        return rev