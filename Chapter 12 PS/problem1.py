# This is a beginner file-handling exercise.
# The program tries to open and read three files: 1.txt, 2.txt, and 3.txt.
# The goal is to practice reading files and handling errors safely.
# If a file exists, its contents are printed.
# If a file is missing, the program does not crash because the exception is caught.
# Instead, Python shows the error message, and the program continues to the next file.

# Try to open and read 1.txt
try:
    with open("1.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

# Try to open and read 2.txt
try:
    with open("2.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

# Try to open and read 3.txt
try:
    with open("3.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

# This final line shows that the program finishes after trying all files.
print("Thank you!")