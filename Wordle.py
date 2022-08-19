import random
import sys    #provides various functions and variables that are used to manipulate different parts of the Python runtime environment
from termcolor import colored    #termcolor used to format output in the terminal
import nltk
# nltk.download('words')
from nltk.corpus import words
# from PyDictionary import PyDictionary
import enchant


def print_menu():
    print("Welcome to Wordle")
    print("Type in a 5 letter word and press ENTER\n")

def read_random_word():
    with open("wordlis.txt") as f:
        wordlis = f.read().splitlines()
        return random.choice(wordlis)
    
nltk.data.path.append('/work/wordlis')
word_list = words.words()
wordlis_five = [word for word in word_list if len(word) == 5]

print_menu()
play_again = ""
while play_again != "n":
    #word = read_random_word()
    word = random.choice(wordlis_five)

    for guess in range(1, 7):
        d = enchant.Dict("en_US")
        g_w = input().lower()
        guess_word = g_w
        valid_word = d.check(g_w)
        
        if not valid_word:
            while not valid_word:
                print("Enter a valid word present in the English Dictionary")
                d = enchant.Dict("en_US")
                g_w = input().lower()
                guess_word = g_w
                valid_word = d.check(g_w)
                # if g_w == "":
                #     valid_word = 1        #condition if we enter without typing in a word

        if valid_word:
            sys.stdout.write('\x1b[1A')     #escape sequence that moves our terminal pointer up to the previous line
            sys.stdout.write('\x1b[2K')     #moves upto the previuos guess and erases it so we can guess our word

            for i in range(min((len(guess_word), 5))):
                if guess_word[i] == word[i]:
                    print(colored(guess_word[i], 'green'), end = "")  #we want to print out the letter but it won't go to a new line
                elif guess_word[i] in word:
                    print(colored(guess_word[i], 'yellow'), end = "")
                else:
                    print(guess_word[i], end = "")
                        
            print()
            if guess_word == word:
                print(colored(f"Congratulations! You have guessed the wordle in {guess} tries", 'red'))
                break
            elif guess == 6:
                print(f"Sorry, the wordle was...{word}")
    
    play_again = input("Do you want to play again? Type n to exit")
                