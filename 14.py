#Question 14
c = 65
for i in range(5):
    for j in range(5):
        if j <= i:
            print(chr(c), end="  ")
    c += 1
    print()
