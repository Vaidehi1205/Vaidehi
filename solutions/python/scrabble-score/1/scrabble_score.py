def score(word):
    point_1 = ['a','e','i','o','u','l','n','r','s','t']
    point_2 = ['d','g']
    point_3 = ['b','c','m','p']
    point_4 = ['f','h','v','w','y']
    point_5 = ['k']
    point_8 = ['j','x']
    point_10 = ['q','z']

    w = list(word.lower())

    sum = 0

    for i in range(len(w)):
        if w[i] in point_1:
            sum += 1
        elif w[i] in point_2:
            sum += 2
        elif w[i] in point_3:
            sum += 3
        elif w[i] in point_4:
            sum += 4
        elif w[i] in point_5:
            sum += 5
        elif w[i] in point_8:
            sum += 8
        elif w[i] in point_10:
            sum += 10 

    return sum
