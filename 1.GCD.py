# define a function
def computeGCD(x, y):
# Find and choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
    return gcd
str1=input("Enter first number: ")
num1 = int(str1)
str2=input("Enter second number: ")
num2 = int(str2)
print("The G.C.D. of", num1,"and", num2,"is", computeGCD(num1, num2))
