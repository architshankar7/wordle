# A '+' below the letter indicates correct letter with the correct placement
#A '*' below the letter indicates the letter is contained in the word, in a different position
#A 'X' below the letter indicates the letter does not appear in the word
#to do list
#1. fix guesses with two of the same letter problems
#2. add information column for letters in the word, that are in the wrong place
#3. 
#4. 
#5. 
import os
import random
#function to clear the console log, thereby hiding prior inputs

def clearConsole():
    os.system('clear')

clearConsole()
wrong = ""
incorrect = False
p1word = ""
p2word = ""
word = ""
wordStatus = list("_____")
indicator = list("_____")
guess = ""
guesses = 0
complete = False
choice = ""

print("RULES")
print("=====")
print("A '+' below a letter indicates the corresponding letter is in the correct position.")
print("A '*' below a letter indicates the corresponding letter is contained in the word, in a different position.")
print("A 'X' below a letter indicates the corresponding letter does not appear in the word.")
while choice != "S" and choice != "M":
    choice = input("Singleplayer or Multiplayer(s or m)?: ")
    choice = choice.upper()
clearConsole()
#user chooses singleplayer
if choice == "S":
    # Open file with 5 letter words in read mode
    with open("5LetterWords.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
    
        # assign selected string as word
        word = (random.choice(words))
        word = word.upper()
    print("A random 5-letter word has been generated!")
    print("5 letter word guesses only!")
    #Player begins guessing word
    while complete == False and guesses != 6:
        guesses += 1
        while len(guess) != 5 or guess.isalpha() == False:
            guess = input()
        guess = guess.upper()
        for i in range(5):
            incorrect = True
            for j in range(5):
                    if guess[i] == word[j]:
                        indicator[i] = '*'
                        incorrect = False
                    elif incorrect == True:
                        indicator[i] = 'X'
            if incorrect == True and wrong.count(guess[i]) == 0:
                wrong = wrong + guess[i]
            if guess[i] == word[i]:
                wordStatus[i] = guess[i]
                indicator[i] = '+'
        print(''.join(indicator) + "||" + "Letters not in the word: " + wrong + "||" + "Current correct placement status: " + ''.join(wordStatus) + "||")
        indicator = list("_____")
        if guess == p2word:
            print("Congratulations! You figured out the word!")
            complete = True
        guess = ""
else:
#user chooses multiplayer
    while len(p1word) != 5 or p1word.isalpha() == False:
        p1word = input("Enter word for player 1: ")
        if len(p1word) != 5:
            print("Your word must be 5 letters!")
        if p1word.isalpha() == False:
            print("Your word must only contain letters!") 
    p1word = p1word.upper()
    clearConsole()
    while len(p2word) != 5 or p2word.isalpha() == False:
        p2word = input("Enter word for player 2: ")
        if len(p2word) != 5:
            print("Your word must be 5 letters!")
        if p2word.isalpha() == False:
            print("Your word must only contain letters!") 
    p2word = p2word.upper()
    clearConsole()
    #player 2 guesses player 1's word
    print("Player 2 guesses Player 1's word.(5 letter word guess)")
    while complete == False and guesses != 6:
        guesses += 1
        while len(guess) != 5 or guess.isalpha() == False:
            guess = input()
        if len(guess) != 5 or guess.isalpha() == False:
            print("Your guess must be a 5 letter word!")
        guess = guess.upper()
        for i in range(5):
            incorrect = True
            for j in range(5):
                    if guess[i] == p1word[j]:
                        indicator[i] = '*'
                        incorrect = False
                    elif incorrect == True:
                        indicator[i] = 'X'
            if incorrect == True and wrong.count(guess[i]) == 0:
                wrong = wrong + guess[i]
            if guess[i] == p1word[i]:
                wordStatus[i] = guess[i]
                indicator[i] = '+'

        print(''.join(indicator) + "||" + "Letters not in the word: " + wrong + "||" + "Current correct placement status: " + ''.join(wordStatus) + "||")
        indicator = list("_____")
        if guess == p1word:
            print("Congratulations! You figured out the word!")
            complete = True
        if guesses == 6 and complete == False:
            print("You failed to guess the word...")
        guess = ""
    print("Player 1 guesses Player 2's word.")
    #initialize variables from previous guesses
    guesses = 0
    complete = False
    wordStatus = list("_____")
    indicator = list("_____")
    guess = ""
    #player 1 guesses player 2's word
    while complete == False and guesses != 6:
        guesses += 1
        while len(guess) != 5 or guess.isalpha() == False:
            guess = input()
        if len(guess) != 5 or guess.isalpha() == False:
            print("Your guess must be a 5 letter word!")
        guess = guess.upper()
        for i in range(5):
            incorrect = True
            for j in range(5):
                    if guess[i] == p2word[j]:
                        indicator[i] = '*'
                        incorrect = False
                    elif incorrect == True:
                        indicator[i] = 'X'
            if incorrect == True and wrong.count(guess[i]) == 0:
                wrong = wrong + guess[i]
            if guess[i] == p2word[i]:
                wordStatus[i] = guess[i]
                indicator[i] = '+'
        #print(''.join(wordStatus))
        print(''.join(indicator) + "||" + "Letters not in the word: " + wrong + "||" + "Current correct placement status: " + ''.join(wordStatus) + "||")
        indicator = list("_____")
        if guess == p2word:
            print("Congratulations! You figured out the word!")
            complete = True
        guess = ""