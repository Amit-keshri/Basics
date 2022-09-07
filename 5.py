#Question 5
cr_rate = input("enter credit rate (good/bad) ")
price = 60000
if cr_rate == "good":
    price = (price*10) / 100
else:
    price = (price*20) / 100
print("down payment = ", price)