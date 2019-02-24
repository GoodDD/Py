import math
def square(a):
    result = tuple()
    p = a*4
    s = a**2
    d = round(a * math.sqrt(2), 3)
    result = list(result)
    result.append("Perimeter: " + str(p))
    result.append("Square area: " + str(s))
    result.append("Diagonal: " + str(d))
    result = tuple(result)
    return "Square with side " + str(a) + " has: " + str(result)

print(square(27))
    
    
