from math import factorial
from math import cos
from math import sin
def f(x):
    if x > 5:
        return min(1,(2 * sin(x)))
    elif x < 0:
        i = 1
        a = 0
        while i < 8:
            a = a + (x**(i - 1) / factorial(i))
            i += 1
        return a
    else :
        return (15 + (cos(x) ** 6)**0.5)

a = float(input("число a"))
b = float(input("число b"))
print(max(f(a),f(b)) - f(3))