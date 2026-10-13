n = int(input("Enter a Number :"))

product = 1
for i in range(1,n+1):
    product *= i
print("The Factorial of number", n, "is:", product)