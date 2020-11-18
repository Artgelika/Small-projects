###################################################################
###################### guess random number ########################
import numpy as np
sentence1 = "# Give me a number in range 1-100 #"
sentence2 = "# Write a number which you like: "
sentence3 = "# Wrong number, you have {} chances"

LENGTH = max(len(sentence1), len(sentence2), len(sentence3))
CHANCE = 3
print("#"*LENGTH)
print(sentence1)

rand_num = np.random.randint(100)

while (CHANCE>0):
    in_number = input(sentence2) 
    in_number = int(in_number)
    
    if (in_number == rand_num):
        print("Good job!")
        break
    else:
        if CHANCE > 2:
            CHANCE -= 1
            print("# Wrong number, you have {} chances#".format(CHANCE))
            print("Random number is {} than yours".format("bigger" if in_number < rand_num else "smaller"))
        elif CHANCE == 2:
            CHANCE -= 1
            print("# Wrong number, you have {} chance #".format(CHANCE))
            print("Random number is {} than yours".format("bigger" if in_number < rand_num else "smaller"))
        else:
            print("# Game over, the number was: ", rand_num)
            break
            
print("#"*LENGTH)

 
