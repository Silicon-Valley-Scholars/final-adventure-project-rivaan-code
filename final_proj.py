import random #Import at least one Python library (SESSION 3)
import math

# This project uses print function (SESSION 1)
# This project uses variables (SESSION 1)

# This is the lists of the the easy and hard qeustions.(Include at least one list (SESSION 4))
easy = ["4+5", "7 + 6" , "8 + 19" , "9+9" , "45 / 9", "-33-54", "20 / 5", "59+97" ,"67+190","4 +78" ,"123 - 24 ", "43 * 2", "11 * 11", "258 - 18"]
hard = ["math.sqrt(256)" , "4**4", "min(12,78,32,56)" ,  "5 * 4 + 9 / 3", "45 - (33 + 12) * 5", "pow(3,5)", "math.sqrt(169)","100 / 40", "45 * 45" ] 

# This function randomly chooses the question from the list and returns.

# This function fulfills following items from project requirement list
# use of if / else (conditional logic) (SESSION 2)
# Create and use at least one function of your own (SESSION 5)
# Use at least one function from that library in your game (SESSION 3)
def get_question(choice):
    equation = 0
 
    questions = []
    if choice == "1":
        questions = easy
    else:
        questions = hard

   #  (SESSION 3) -The random.choice function to randomly choose the questions from the easy or hard list.
    return random.choice(questions)

# Welcome message
print("******WELCOME TO MY ADVENTOROUS MATH TRIVIA GAME******")

# variable storing player
name = input("Enter your name : ")
print("WELCOME " , name)

print("\n-----You are LOST and stuck in a MAZE. You need to find a TOOL or RIDE to way back home.-----")

# Loop to play the game  -   Use at least one loop(session 4)
while(input("\nDo you want to play (y/n) :") == "y"):
    print("\nYou have choose easy or hard adventure ? \n Type 1 for Easy  \n Type 2 for Hard")
    path = input("Enter your path choice : ")  # At least one user input (like a decision or name) (SESSION 2)
    if path == "1":
        print("\nYou need to cross a swamp lake to get a boat and row back a safe river to home.")
        print("You have 3 hanging veins to cross. If you answer wrong, the veins disappear. If you are lucky, questions repeat... Good Luck!!")
        expression = get_question(path)
        answer = int( input("\nSOLVE QUESTION 1: "+ expression +" :")   )
        if answer == eval(expression):
            vein_of_gold = 1
            print("\nCongratulations..  You have" , vein_of_gold ,"vein of gold")
            expression = get_question(path) 
            answer = int(input("\nSOLVE QUESTION 2: "+ expression + " :"))
            if answer == eval(expression) :
                veins_of_gold = vein_of_gold + 1 #At least one use of math operators (SESSION 2)
                print("\nCongratulations... You have" , veins_of_gold ,"veins of gold")
                expression = get_question(path)
                answer  = int(input("\nSOLVE QUESTION 3: "+ expression + " :"))
                if answer == eval(expression):
                    veins_of_gold = veins_of_gold + 1
                    print("\nCongratulations ... You have" , veins_of_gold ,"veins of gold")
                    print("You reached other side of lake and got the boat. You can row back safely across the river back home.")
                else:
                    print("\nYou got stuck in the sticky mud pit!!")
                    print("You have 2 veins of gold ,you lose!")
            else:
                    print("\nYou are encircled with crocodiles!!")
                    print("You have 1 vein of gold , you lose!")
        else:
                print("\nYou got trapped in veins and roots in lake!!!")
                print("You have 0 veins of gold ,you lose!")
    elif path == "2":
        print("\nYou need to Cross Volcano Lake and your rescures are waiting on other end..")
        print("You have 3 floating stones to cross, which will sink if you answer wrong. If you are lucky, questions repeat... Good Luck!!")
        expression = get_question(path)
        answer = float(  input("\nSOLVE QUESTION 1: "+ expression +" :")   )
        if answer == eval(expression):
            expression = get_question(path)
            floatingstone = 1
            print("\nCongratulations..  You have",floatingstone ," floating stone")
            answer = float(input("\nSOLVE QUESTION 2: "+ expression + " :"))
            if answer == eval(expression) :
                expression = get_question(path)
                floatingstone = floatingstone + 1
                print("\nCongratulations.. You have  ",floatingstone ," floating stones")
                answer  = float(input("\nSOLVE QUESTION 3: "+ expression + " :"))
                if answer == eval(expression):
                    floatingstone = floatingstone + 1
                    print("\nCongratulations ... You have  ",floatingstone ," floating stones")
                    print("You reached the other side off the lava lake . And you can safely go home. ")
                else:
                    print("\nYou got fell down into lava lake...!")
                    print("You have 2 floating stones ,you lose!")
            else:
                print("\nYou are attacked by lava bombs!!")
                print("You have 1 floating stone , you lose!")
        else:
            print("\nYou got trapped Volcano Smoke!!!")
            print("You have 0 floating stones ,you lose!")

    else: print("Invalid Choice...")

print("\n--------Thank you for playing-------\n")
