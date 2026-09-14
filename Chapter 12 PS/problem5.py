# Ask the user to enter a number and convert it to an integer.
# int(...) changes the input string into a numeric value so we can do math.
n = int(input("Enter a number: "))

# Build a list of multiples from 1 to 10 for the entered number.
# Example: if n = 5, table becomes [5, 10, 15, ..., 50].
table = [n * i for i in range(1, 11)]

# Open the file in append mode so new content is added without deleting old data.
# 'a' means "append": Python writes at the end of the file, keeping previous content intact.
# Write the table as text into 'table.txt'.
with open("table.txt", "a") as f:
    # f.write(...) saves the text to the file.
    # f"Table of {n}: {str(table)} \n" creates a formatted string like: "Table of 5: [5, 10, 15, ...]"
    # The \n moves the cursor to the next line after writing, so each table is written on a new line.
    f.write(f"Table of {n}: {str(table)} \n")