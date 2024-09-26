import math

def num(x):
    if x >= 1:
        return (2/x) + 2.31 * math.pow(math.e, 2 * x)
    elif x > -1 and x < 1:
        return math.asin(0.2 * x + 0.3)
    elif x <= -1:
        return math.cos(x + 0.4 * math.log(abs(x + 0.2), math.e))
    
x = float(input("x = "))
print(num(x))