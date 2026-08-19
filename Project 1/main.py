import random


computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice (s=snake, w=water, g=gun): ")
youDict = { "s" : 1, "w" : -1, "g" : 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

#By now we have 2 numbers(variables), you and computer, 
# which can be -1, 0 or 1. Now we will compare them to find the winner.

print(f"You chose: {reverseDict[you]}")
print(f"Computer chose: {reverseDict[computer]}")

if(computer == you):
    print("It's a tie!")
else:
    if(computer == -1 and you == 1):
        print("You win!")
    elif(computer == 1 and you == -1):
        print("You lose!")
    elif(computer == -1 and you == 0):
        print("You lose!")
    elif(computer == 0 and you == -1):
        print("You win!")
    elif(computer == 0 and you == 1):
        print("You lose!")
    elif(computer == 1 and you == 0):
        print("You win!")