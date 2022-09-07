#Question 4
sum_of_sq = 0
n = int(input("enter  a number  : "))
for i in range(1, n+1):
    sq = i**2
    sum_of_sq = sum_of_sq + sq
print("sum of squares of first", n, "natural number is : ", sum_of_sq)
