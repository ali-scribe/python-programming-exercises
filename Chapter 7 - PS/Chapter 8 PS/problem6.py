def inch_to_cms(inch):
    return inch * 2.54

n = int(input("Enter value in inches: "))
#here f is used to format the string and include the value of inch_to_cms(n) in the output
print(f"The corresponding value in cms is: {inch_to_cms(n)}")