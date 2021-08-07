def equilateral(sides):
    a, b, c = sides
    return all(side > 0 for side in sides) and (a == b and b == c and c == a)


def isosceles(sides):
    a, b, c = sides
    return all(side > 0 for side in sides) and (a == b or b == c or c == a)


def scalene(sides):
    a, b, c = sides
    return all(side > 0 for side in sides) and a != b != c
