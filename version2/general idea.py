import random
import nltk
from nltk.corpus import words

nltk.download('words')

def choose_word_from_nltk():
    english_words = words.words()
    return random.choice(english_words)


def display_word(word, guessed_letters):
    # Function to display the word with correctly guessed letters
    pass

def display_hangman(wrong_guesses):
    # Function to display the hangman figure based on the number of wrong guesses
    pass

def get_user_guess():
    # Function to get a valid user guess
    pass

def play_hangman():
    # Main game loop
    pass

if __name__ == "__main__":
    play_hangman()


