# Ask the user to enter a number.
n = int(input("Enter a number: "))

# Create a list containing the multiplication table of n from 1 to 10.
table = [n * i for i in range(1, 11)]

# Display the resulting multiplication table.
print(table)