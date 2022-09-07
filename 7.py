#Question 7
a = int(input("enter a "))
b = int(input("enter b "))
c = int(input("enter c "))
if a > b:
    if a > c:
        print(a, "is the largest")
    else:
        print(c, "is the largest")
else:
    if b > c:
        print(b, "is the largest")
    else:
        print(c, "is the largest")
