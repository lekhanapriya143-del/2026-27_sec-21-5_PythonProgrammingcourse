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


a = 7
b = 2
print("addition:",a+b)
print("subtraction:",a-b)
print("multiplication:",a*b)
print("division:",a/b)
print("modulus:",a%b)
print("floor division:",a//b)
print("exponent:",a**b)




a=19
b=22
result = a==b
print("result of",a,"==",b,"is:",result)
result = a!=b
print("result of",a,"!=",b,"is:",result)
result= a<b
print("result of",a,"<",b,"is:",result)
result =a>b
print("result of",a,">",b,"is:",result)
result = a<=b
print("result of",a,"<=",b,"is:",result)
result=a>=b
print("result of",a,">=",b,"is:",result)
