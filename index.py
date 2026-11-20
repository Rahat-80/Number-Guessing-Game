import random

print("Welcome to the Number Guessing Game!")
print("I have selected a random number between 1 and 100. Try to guess it!")
number = random.randint(1, 100)
guess = None
attempts = 0

while guess != number:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")