print("Heyy")

# This is a simple Python script that prints "Heyy" to the console. You can run this code in any Python environment to see the output.

#New code to print HII score

import random

def game():
    print("You are playing the game..")
    score = random.randint(1,62)
    #Fetch the hiscore
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
            
    print(f"Your score is: {score}")
    if(score > hiscore):

        with open("hiscore.txt","w") as f:
            f.write(str(score))

    return score

game()        