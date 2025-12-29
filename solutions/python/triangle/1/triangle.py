def is_triangle(sides):
    a, b, c = sides
    return a + b > c and a + c > b and b + c > a and min(sides) > 0


def equilateral(sides):
    if not is_triangle(sides):
        return False
    return len(set(sides)) == 1   


def isosceles(sides):
    if not is_triangle(sides):
        return False
    return len(set(sides)) <= 2   


def scalene(sides):
    if not is_triangle(sides):
        return False
    return len(set(sides)) == 3   
