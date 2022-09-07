#Question 2
for i in range(6):
    for j in range(i):
        if j <= i:
            print("*", end="  ")
    print("\n")
