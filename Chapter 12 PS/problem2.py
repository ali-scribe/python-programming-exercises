# Create a list of numbers from 1 to 8.
l = [1,2,3,4,5,6,7,8]

# Loop through each item with its index position.
for i, item in enumerate(l):
    # Print the values at indexes 2, 4, and 6.
    if i == 4 or i == 6 or i == 2:
        print(item)