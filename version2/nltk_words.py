# nltk_words.py
import random
import nltk
from nltk.corpus import words

#nltk.download('words')

def choose_word_from_nltk():
    english_words = words.words()
    return random.choice(english_words)
#test
x=choose_word_from_nltk()
print(x,type(x))