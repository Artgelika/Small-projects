### import libraries
import numpy as np

### data
animals = ["orka", "lew", "ćma", "pingwin", "struś", "krowa", "pająk", "skorpion", "mucha", "pies", "konik polny", "delfin", "koziorożec", "alpaka", "bocian", "papuga", "wieloryb", "tarantula", "świnia"] # it would be csv later (?)
chances = 3 # number of chances in game1

### interface
line0 = "Wybierz, co chcesz zrobić:"
line1 = "1. New game"
line2 = "2. Exit"

print("#" * max(len(line1), len(line2), len(line0)))
print(line0)
print(line1)
print(line2)
print("#" * max(len(line1), len(line2), len(line0)))

### draw the word from given above
random_num = np.random.randint(len(animals))
# print(random_num)
word_to_hangman = animals[random_num]
# print(word_to_hangman)

### checking the gamer's choice (on interface)
########################################
klik  = input() # somebodys choose 1 or 2
chance1 = 2
while (chance1 > 0):
    try:
        if (int(klik) > 2 or int(klik) < 1):
            print("Wrong choice\n Try again\n")
            klik  = input()
            chance1 -= 1
        else:
            chance1 = 0
    except: # if it was something other than single int number in range <1,2>
        print("That's not a number!")
        quit()
##########################################

### print lines
def lines(word):
    word_copy = list(word)
    strr = ""
    for i in range(len(word_copy)):
        if word_copy[i].isalpha():
            word_copy[i] = "_"
        elif word_copy[i] == " ":
            word_copy[i] = " "
    
    strr = ""
    for el in word_copy:
        strr += el 
        strr += " "
    return strr


if (int(klik) == 1):
    line = lines(word_to_hangman) # it is a string
    print(line)
    line = list(line)

    while (chances > 0): # if game is still alive
        letter_from_user = input("Give a letter: ")
        if letter_from_user in line:
            print("You'd already wrote it")

        if letter_from_user in word_to_hangman:
            coun = word_to_hangman.count(letter_from_user)
            if coun == 1:                                 # if a letter is once
                i = word_to_hangman.index(letter_from_user)
                line[2*i] = letter_from_user
            else:                                         # if a letter is multiple times
                for i in range(len(word_to_hangman)):
                    if(word_to_hangman[i] == letter_from_user):
                        line[2*i] = letter_from_user
            

            lin = ""
            for el in line:
                lin += el 
            print(lin)
            if "_" not in lin:
                print("Wygrana!")
                quit()
            
        else:
            chances -= 1
            print("That letter is not in that word")
            if chances >= 2:
                print("You have: {} chances".format(chances))
            elif chances == 1:
                print("You have: {} chance".format(chances))
            else:
                print("You have no chances.\n The word was: ", word_to_hangman)

elif klik==2:
    quit()


