#trangle - get area of a trangle a+b+c

def triangle(a, b, c):
    trangle = a + b + c
    if trangle > 180:
        return "A triangle cannot have angles that more then 180°"
    elif trangle < 180:
        return "A triangle cannot have angles that less then 180°"
    else:
        return trangle

def findthirdangle(a,b):
    thirdangle = a + b
    angle = 180
    findangle = angle - thirdangle

    if findangle <= 0 or findangle > 180:
        return "A triangle cannot have an angle of " + str(findangle) + "°. The sum of all all angles must equal 180°."
    else:
        return findangle

