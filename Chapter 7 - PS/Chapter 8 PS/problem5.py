def pattern(n):
    if (n == 0):
        return #can be used to end the function without returning any value
    print("*" * n)
    pattern(n - 1)

pattern(3)    