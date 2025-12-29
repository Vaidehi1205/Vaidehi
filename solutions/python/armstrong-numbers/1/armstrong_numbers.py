def is_armstrong_number(number):
    num = [int(d) for d in str(number)]

    am = [0,1,2,3,4,5,6,7,8,9]
    a=0

    if number in am :
        return True
    else:
        for n in num:
            a += n ** len(num)
            
        if int(a) == int(number):
            return True
        else:
            return False



    
