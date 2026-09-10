n = int(input("Enter a number: "))

# Loop through each row
for i in range(1, n + 1):

    # If it's the first or last row, print all stars
    if i == 1 or i == n:
        print("*" * n, end="")

    # Otherwise, print a hollow row
    else:
        print("*", end="")          # Left border
        print(" " * (n - 2), end="") # Middle spaces
        print("*", end="")          # Right border

    # Move to the next line after each row
    print()