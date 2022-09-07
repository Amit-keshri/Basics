#Question 11
print(" \nCALCULATOR\n")
a = int(input("a = "))
b = int(input("b = "))
op = (input("op = "))
if op == '+':
    print(a, "+", b, "=", a+b)
elif op == '-':
    print(a, "-", b, "=", a-b)
elif op == 'x':
    print(a, "x", b, "=", a*b)
elif op == '/':
    print(a, "/", b, "=", a/b)
else:
    print("invalid operator")
