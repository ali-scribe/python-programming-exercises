n = int(input("Enter a number: "))

product = 1
for i in range(1, n+1): 
#n+1 because we want to include n in the range, usually range goes up to n-1
    product = product * i

print(f"The factorial of {n} is {product}")