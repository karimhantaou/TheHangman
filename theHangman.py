import os
import time
import random
#from english_words import get_english_words_set

#Return a random english word from the words.txt file
def getRandomWord():
    '''
    english_words = get_english_words_set(['web2'], lower=True)
    english_words = list(english_words)
    return english_words[random.randint(0, len(english_words))]
    '''
    english_words = f = open('words.txt')
    english_words = f.read().splitlines()
    f.close()

    return english_words[random.randint(0, len(english_words))]


#Test if each letter have been found
def isFound(word, found_letter):
    for char in word:
        if char.lower() not in found_letter.lower():
            #Return false if one letter isn't
            return False
    #Return true if none is missing
    return True

#Test if a given letter is in the word to find, True if yes false if not or already found
def isIn(word, found_letter, letter):
    if letter.lower() in word.lower() and letter.lower() not in found_letter :
        return True
    else:
        return False

#Print the found letters
def showFoundLetters(word, found_letter):
    result = ""
    for char in word :
        #Print the char if is found
        if char.lower() in found_letter.lower():
            result += char + " "
        #Print _ if not
        else:
            result += "_ "
    return result

def isGameOver(penalties):
    if penalties >= 12:
        return True
    else:
        return False

def gameOver(word, rush, words_count):
    os.system("cls")
    print("GAME OVER")
    print("The word was : ", word)
    if rush:
        print("Total words found : ", words_count)
        user = input("Your username : ")
        insertScore(user, words_count)

def victory(word, penalties):
    os.system("cls")
    print("Congratulation you won !")
    print("You found the word : ", word)

def wordChoice(r):
    if  r == "yes" or r == "y":
        return getRandomWord()
    else:
        return input("Write a word : ")

def start():
    os.system("cls")
    print("THE HANGMAN !")
    print("Choose a game mode.")

    print("1. Normal")
    print("2. Rush")
    print("3. Rush Scrore Board")

    x = input("Game mode : ")

    if x == "1":
        game(False, 0)
    if x == "2":
        game(True, 0)
    if x == "3":
        showScore()

def showScore():
    scoreBoard = f = open('score.txt')
    scoreBoard = f.read().splitlines()
    f.close()

    os.system("cls")
    print("SCORE BOARD")

    i = 1
    for score in scoreBoard:
        print(i,".",score, "words")
        i+=1

def insertScore(username, score):
    with open("score.txt", "a") as f:
        
        newEntry = username + " : " + str(score) + "\n"
        
        f.write(newEntry)

#Mode False normal, mode True rush
def game(mode, found_words):

    os.system("cls")

    found_letters = ""
    used_letters = ""
    penalties = 0

    if not mode : r = input("Get a random word ? (yes/no) : ")
    else: r = "y"

    word = wordChoice(r)
    
    while True:
        os.system("cls")

        if mode : print("Words found : ", found_words)

        printTheHangman(penalties)

        print("The Hangman ! ", showFoundLetters(word, found_letters))

        print("Penalties: ", penalties, "/12")

        print("Already used letters : ", used_letters)

        l = input("Give a letter : ")

        if l not in used_letters:
            used_letters += l

        if isIn(word,found_letters, l):
            found_letters += l
        else:
            penalties +=1

        if isFound(word, found_letters):
            victory(word, penalties)
            if mode : game(True, found_words + 1) 
            break

        if isGameOver(penalties):
            if mode : gameOver(word, True, found_words)
            else : gameOver(word, False, 0)
            break

def printTheHangman(penalties):
    if penalties >= 4:
        print("+---+")
    if penalties >=3  and penalties <5:
        print("|")
        print("|")
        print("|")   
    if penalties >=2 and penalties <5:
        print("|")
        print("|")
        print("|") 

    if penalties == 5:
        print("|   |")
        print("|")
        print("|") 
        print("|")
        print("|")
        print("|") 

    if penalties == 6:
        print("|   |")
        print("|   |")
        print("|") 
        print("|")
        print("|")
        print("|") 

    if penalties == 7:
        print("|   |")
        print("|   |")
        print("|   O") 
        print("|")
        print("|")
        print("|") 

    if penalties == 8:
        print("|   |")
        print("|   |")
        print("|   O") 
        print("|   |")
        print("|")
        print("|") 

    if penalties == 9:
        print("|   |")
        print("|   |")
        print("|   O") 
        print("|  /|")
        print("|")
        print("|") 

    if penalties == 10:
        print("|   |")
        print("|   |")
        print("|   O") 
        print("|  /|\ ")
        print("|")
        print("|") 

    if penalties == 11:
        print("|   |")
        print("|   |")
        print("|   O") 
        print("|  /|\ ")
        print("|  /")
        print("|") 

    if penalties == 12:
        print("|   |")
        print("|   |")
        print("|   O") 
        print("|  /|\ ")
        print("|  / \ ")
        print("|") 

    if penalties >= 1:
        print("======")

start()
