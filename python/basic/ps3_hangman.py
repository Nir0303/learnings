# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

import string
def isWordGuessed(secretWord, lettersGuessed):
    secretWord=list(secretWord)
    lettersGuessed=set(lettersGuessed)
    cnt=0
    for i in lettersGuessed:
        cnt+=secretWord.count(i)
    return len(secretWord)==cnt


def getGuessedWord(secretWord, lettersGuessed):
    secretWord=list(secretWord)
    lettersGuessed=list(set(lettersGuessed))
    x='_'*len(secretWord)
    x=list(x)
    for i in range(len(lettersGuessed)):
        for j in range(len(secretWord)):
            if secretWord[j]==lettersGuessed[i]:
                x[j]=secretWord[j]
    return ''.join(x)


def getAvailableLetters(lettersGuessed):
    lowercase=string.ascii_lowercase
    lowercase=set(lowercase)-set(lettersGuessed)
    return ''.join(sorted(list(lowercase)))

    

def hangman(secretWord):
    print "Welcome to the game, Hangman!"
    x=secretWord
    print "I am thinking of a word that is {} letters long.".format(len(x))
    guesses=8
    success=0
    t=''
    while guesses>0 and success==0:
        print "-------------"
        print "You have {} guesses left.".format(guesses)
        print "Available letters: {}".format(getAvailableLetters(t))
        char= raw_input("Please guess a letter:") 
        
        if char in t:
            print "Oops! You've already guessed that letter: {}".format(getGuessedWord(x,t))
            continue
        else:
            t+=char
            if char in x:
                print "Good guess: {}".format(getGuessedWord(x,t))
            else:
                guesses-=1
                print "Oops! That letter is not in my word: {}".format(getGuessedWord(x,t))
        if isWordGuessed(x,t):
            break
            
    if guesses>0:
        print "Good guess: {}".format(x)
        print("------------")
        print("Congratulations, you won!")
    else:
        print("------------")
        print("Sorry, you ran out of guesses. The word was else.")

hangman(chooseWord(wordlist))



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
