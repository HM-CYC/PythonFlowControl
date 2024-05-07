#Write a Python program that prompts the user to guess a secret number between 1 and 100.
# Keep prompting until they guess it correctly. Print "Correct!" when they guess it right.

import random

secret_number = random.randint(1, 100)
guess = None

while guess != secret_number:
    guess = int(input("Guess the secret number: "))
    if guess == secret_number:
        print("Correct!")
        break
