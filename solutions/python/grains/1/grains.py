def square(number):
    s = 1
    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")
    else:
        for i in range(number):
            if i == 0:
                s = 1
            else:
                s*=2

    return s 


def total():
    return sum(square(i) for i in range(1, 65))