import random
import string

words = ["loan", "nose", "jungle", "Dog"]


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_letters)
    used_letter = set()
    lives = 6
    while len(word_letters) > 0 and lives > 0:

        print("You have", lives,
              "lives left and you have used these letter:", ' '.join(used_letter))
        word_list = [
            letter if letter in used_letter else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))
        user_letter = input("guess letter:").upper()
        if user_letter in alphabet-used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives-1
        elif user_letter in used_letter:
            print("You have already user that letter")
        else:
            print("You have enter invalid word")

    if lives == 0:
        print('You have died. The word was ', word)
    else:
        print("You have guessed the word", word, '!!')


hangman()
