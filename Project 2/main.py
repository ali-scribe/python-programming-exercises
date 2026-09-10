import random

# Pick a random number the player must guess between 1 and 100.
n = random.randint(1, 100)

# Set the user's current guess to a value that ensures the loop starts.
a = -1

# Count how many tries the player has used.
guesses = 1

# Keep asking until the player guesses the target number.
while a != n:
    a = int(input("Enter a number: "))

    # Give hints based on whether the guess is too high or too low.
    if a > n:
        print("Lower number please")
        guesses += 1

    elif a < n:
        print("Higher number please")

# Tell the player they won and show how many attempts it took.
print(f"Congratulations! You guessed the number in {guesses} attempts.")