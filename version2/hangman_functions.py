# hangman_functions.py

import random



def display_word(word, guessed_letters):
    # Function to display the word with correctly guessed letters
    for i in word:
        guessed_letters.append(i)
        for letter in guessed_letters:
            for v in guessed_letters:
                if v==letter:
                    word_g+=letter
                else:
                    word_g+='_'
        print(word_g)
    return guessed_letters
    pass

def display_hangman(wrong_guesses):
    # Function to display the hangman figure based on the number of wrong guesses
    pass

