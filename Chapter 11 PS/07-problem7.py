

n = int(input("Enter a number: "))

for i in range(1, n+1):
  print (" " * (n-i), end="") #Write spaces
  print ("*" * (2*i-1), end="") #Write stars in same line
  print("") #for moving on next line