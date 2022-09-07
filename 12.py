#Question 12
import math
print("enter a, b , c  as in ax2+bx+c")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = b*b - 4*a*c
if d > 0:
    r1 = (-b+math.sqrt(d)) / (2*a)
    r2 = (-b-math.sqrt(d)) / (2*a)
    print("r1 = ", r1, "\nr2 = ", r2)
elif d == 0:
    r = (-b) / (2*a)
    print("both the roots are same \n \t r =", r)
else:
    print("imaginary roots")
