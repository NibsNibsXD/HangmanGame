import random
from words import words
import string
from hangmandraw import HANGMANPICS
from hangmandraw import FIRSTHANGMAN


def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed

    lives = 0
    showlives = 8 - lives

    # getting user input
    while len(word_letters) != 8 and lives != 8:
        showlives = 8 - lives
        print("You have " + str(showlives) + " lives left, You have used these letters: " + " ".join(used_letters))

        #what the current word is (N I _ S)
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("Current word: " + " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives += 1
                print("The letter " + user_letter + " is not in the word")
                if lives == 1:
                    print(FIRSTHANGMAN[0])
                else:
                    print(HANGMANPICS[lives - 2])

        elif user_letter in used_letters:
            print("You already guessed that, try again.")
        else:
            print("Invalid character, try again.")


    if lives != 0:
        print("You died, the word was " + word)
    else:
        print("YAY, YOU GUESSED THE WORD " + word)

hangman()

