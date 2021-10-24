money = int(input("How much money do you have? "))
apple = int(input("What is the price of an apple per piece? "))

maximumNumberofApple = money // apple
chage = money % apple
print(f"you can buy {maximumNumberofApple} apples and your change is ₱{chage: .2f}")