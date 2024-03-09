# hangman_game.py

import eel
import nltk
import random
from hangman_functions import check_letters, display_word 
from nltk_words import choose_word_from_nltk
eel.init('web')
guessed_letters={
    '#':1,
    'a':1,
    'b':0,
    'c':0,
    'd':0,
    'e':1,
    'f':0,
    'g':0,
    'h':0,
    'i':1,
    'j':0,
    'k':0,
    'l':0,
    'm':0,
    'n':0,
    'o':1,
    'p':0,
    'q':1,
    'r':0,
    's':0,
    't':0,
    'u':1,
    'v':0,
    'w':0,
    'x':0,
    'y':0,
    'z':0
    }
word=choose_word_from_nltk().lower()

@eel.expose
def init():
    global word
    global guessed_letters
    word=choose_word_from_nltk().lower()
    guessed_letters={
    '#':1,
    'a':1,
    'b':0,
    'c':0,
    'd':0,
    'e':1,
    'f':0,
    'g':0,
    'h':0,
    'i':1,
    'j':0,
    'k':0,
    'l':0,
    'm':0,
    'n':0,
    'o':1,
    'p':0,
    'q':1,
    'r':0,
    's':0,
    't':0,
    'u':1,
    'v':0,
    'w':0,
    'x':0,
    'y':0,
    'z':0
    }


@eel.expose
def play_hangman(wrongs,letter):
    print(wrongs,letter,word)
    # Main game loop
    #wrongs=0#getwrongs from html
    #word=choose_word_of_nltk()#Word add function
    displayed_word=""
    global guessed_letters
    disp_w,mes,wrongs=check_letters(word,guessed_letters,letter,wrongs)  
    #call function to display hangman
    return f"{wrongs},{mes},{disp_w}"

@eel.expose
def Win_or_loss(geussed_word):
    global word
    #print(geussed_word)
    if word==geussed_word:
        return "True"
    else:
        return "False"

    pass

eel.start('index.html',mode="firefox")



