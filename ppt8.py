principal=float(input("Enter the principal amount: "))
rate=float(input("Enter the rate of interest: "))  
time=float(input("Enter the time period: "))
simple_interest=(principal*rate*time)/100
print("The simple interest is: ",simple_interest)





principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))
amount = principal * (1 + rate / 100) ** time
compound_intrest = amount - principal - amount
print("Compound Intrest=",compound_intrest)







n = int(input("Enter N: "))

sum = n * (n + 1) // 2

print("Sum of first N natural numbers =", sum)
