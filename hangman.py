import string
from words import choose_word
from images import IMAGES
import random
'''
Important instruction
* function and variable name snake_case -> is_prime
* contant variable upper case PI
'''

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return True (if user guess the world correctly )
      return False (wrong selection)
    '''
    print(secret_word,letters_guessed)
    if(len(secret_word)==len(letters_guessed)):
        return True
    return False

# if you want to test this function please call function -> get_guessed_word("kindness", [k, n, d])


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return string which contain all the right guessed characters
      Example :- 
      if secret_word -> "kindness" and letters_guessed = [k, n, s]
      return "k_n_n_ss"
    '''
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list contains all guessed characters
    returns: 
      it return string which contains all characters except guessed letters
    Example :-
      letters_guessed = ['e', 'a'] then    
      return sting is -> `bcdfghijklmnopqrstuvwxyz`
    '''
    all_chars_atoz=string.ascii_lowercase
    str1=""
    let_guessedString=str1.join(letters_guessed)
    letters_left = [i for i in all_chars_atoz+let_guessedString  if i not in all_chars_atoz or i not in let_guessedString]
    str2=""
    string_Letters_left=str2.join(letters_left)
    return string_Letters_left
def showMan(rem):
    print(IMAGES[rem])

def isValid(letter):

    if(len(letter)==1 and letter.islower()):
        return True
    return False

def hangman(secret_word):
    '''
    secret_word (string) : secret word to guessed by the user.

    Steps to start Hangman:

    * In the beginning of the game user will know about the total characters in the secret_word    

    * In each round user will guess one character 

    * After each character give feedback to the user
      * right or wrong

    * Display partial word guessed by the user and use underscore in place of not guess word    
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(
        str(len(secret_word))), end='\n\n')
    letters_guessed = []
    t=1
    remaining_lives=8
    c=0
    hint_used=False
    while(t==1):
        print("{} lives left".format(remaining_lives))
        if(remaining_lives>0):
            available_letters = get_available_letters(letters_guessed)
            print("Available letters: {} ".format(available_letters))
            guess = input("Please guess a letter: ")
            letter = guess.lower()
            if(letter!="hint" and not isValid(letter)):
                print("Invalid input..Enter again")
                continue
            if(letter=="hint"):
                if hint_used==False:
                    hint_used=True
                    lst=[]
                    print("hint worked")
                    print(available_letters)
                    for i in secret_word:
                        lst.append(i)
                    print(letters_guessed)
                    # secret_word-letters_guessed
                    li_dif = [i for i in lst + letters_guessed if i not in lst or i not in letters_guessed]
                    letter=random.choice(li_dif)

                else:
                    print("Sorry buddy you have used your hint")
                    continue
            if letter in secret_word:
                c+=1
                letters_guessed.append(letter)
                print("Good guess: {} ".format(
                    get_guessed_word(secret_word, letters_guessed)))
                if is_word_guessed(secret_word, letters_guessed) == True:
                    t=0
                    print(" * * Congratulations, you won! * * ", end='\n\n')
            else:
                remaining_lives-=1
                # 7->0
                showMan(8-(remaining_lives+1))
                print("Oops! That letter is not in my word: {} ".format(
                    get_guessed_word(secret_word, letters_guessed)))
                
                
        else:
            t=0
            print("Game Over!!!!You ran out of lives")

# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)
