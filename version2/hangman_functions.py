# hangman_functions.py

import random



def display_word(word, guessed_letters):
    # Function to display the word with correctly guessed letters
    word_display=""
    for i in word:
        if guessed_letters[i]==1:
            word_display=word_display+i
        else:
            word_display=word_display+'_'
    return word_display)
    pass

def check_letters(word, guessed_letters,gussed_letter,wrongs,message=""):
    if gussed_letter in word:
        if guessed_letters[gussed_letter]==1:
            message="word aldready guessed"
            word=display_word(word, guessed_letters)
            return word,message,wrongs
        else:
            message="letter in word"
            word=display_word(word, guessed_letters)
            return word,message,wrongs
    else:
        message="letter is not in word"
        word=display_word(word, guessed_letters)
        return word,message,wrongs+1
    pass
def display_hangman(wrong_guesses):
    # Function to display the hangman figure based on the number of wrong guesses
    pass

