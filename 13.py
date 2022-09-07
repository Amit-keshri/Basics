#Question 13
print("FIRST MATRIX")
r = int(input("enter number of rows "))
c = int(input("enter number of columns "))
M1 = []
print("enter matrix elements \n")
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    M1.append(a)

print("SECOND MATRIX")
M2 = []
print("enter matrix elements \n")
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    M2.append(a)
print("M1 is:")
for i in range(r):
    for j in range(c):
        print(M1[i][j], end=" ")
    print()
print("M2 is:")
M3 = []
for i in range(r):
    a = []
    for j in range(c):
        print(M2[i][j], end=" ")
        b = M2[i][j] + M1[i][j]
        a.append(b)
    M3.append(a)
    print()
print("M1 + M2 is :")

for i in range(r):
    for j in range(c):
        print(M3[i][j], end=" ")
    print()
