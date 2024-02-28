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
    return word_display
    pass

def check_letters(word, guessed_letters,gussed_letter,wrongs,message=""):
    if gussed_letter in word:
        if guessed_letters[gussed_letter]==1:
            message="letter aldready guessed"
            word=display_word(word, guessed_letters)
            return word,message,wrongs
        else:
            message="letter in word"
            guessed_letters[gussed_letter]=1
            word=display_word(word, guessed_letters)
            return word,message,wrongs
    elif guessed_letters[gussed_letter]==1:
        message="letter aldready guessed"
        word=display_word(word, guessed_letters)
        return word,message,wrongs
    else:
        message="letter is not in word"
        word=display_word(word, guessed_letters)
        guessed_letters[gussed_letter]=1
        return word,message,int(wrongs)+1
    pass



#test
'''guessed_letters={
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
'''
#word="hello"

#wrongs=0

#dip_word,mes,wrongs=check_letters(word,guessed_letters,'h',wrongs)

#print(dip_word,mes,wrongs,guessed_letters,sep="\n")
