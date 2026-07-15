...
# sum(1) = 1
# sum(2) = 1 + 2
# sum(3) = 1 + 2 + 3
# sum(4) = 1 + 2 + 3 + 4
# sum(5) = 1 + 2 + 3 + 4 + 5
# sum(n) = 1 + 2 + 3 + ... + n - 1 + n
# sum(n) = sum(n-1) + n
...
# if n == 1, return 1 otherwise return sum(n-1) + n
#so it doesn't become an infinite loop
def sum(n):
    if n == 1:
        return 1
    else:
        return sum(n - 1) + n
    
print(sum(4))