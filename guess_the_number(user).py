# guess the computer(user)
import random as rt


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while (feedback != 'c'):
        if low != high:
            guess = rt.randint(low, high)
        else:
            guess = low
        feedback = input(
            f'Is {guess} too high(H),too low(L),or correct(c)??').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"Yey, the computer guessed the your number,{guess} correctly")


computer_guess(10)
