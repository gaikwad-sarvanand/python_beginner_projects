# Guess the number(computer)
import random as rt


def guess(x):
    random_number = rt.randint(1, x)
    guess = 0
    while (random_number != guess):
        guess = int(input(f"guess a number between 1 and {x} : "))
        if guess < random_number:
            print("Sorry,Guess again.Too low")
        elif guess > random_number:
            print("Sorry,Guess again,Too high")
    print(
        f"Congrats,You have guessed the right number {random_number} correctly")


guess(10)
