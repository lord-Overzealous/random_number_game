# import module - library
import random as rd

# gloabl variable
lenght = None
randomNumb = None
GameOn = None


softwarOn = True




# reinitialise all of the variable
def initialise():
    global lenght
    global randomNumb
    global GameOn


    lenght = 10
    randomNumb = rd.randrange(lenght)
    GameOn = True

    return lenght, randomNumb, GameOn

# porteille - i have to find another name for this function
def porteille():
    # variable 
    global softwarOn


    print("hello Guess the number to win: ")
    exitSoftwar = input("If you whant to exit type (exit or x). \ndo you whant to exit: ")

    if exitSoftwar == "exit" or exitSoftwar == "x":
        softwarOn = False

    return




# MainLoop
while softwarOn:
    porteille()

    initialise()

    while GameOn:
        guess = int(input("type a guess: "))

        if guess == randomNumb:
            print(f"congratulation you win the random number was { str(guess) }\n")
            GameOn = False
            randomNumb = rd.randrange(lenght)

        elif guess < randomNumb:
            print(f"you''r guess of { str(guess) } is smaller than the number try again. \n")
        elif guess > randomNumb:
            print(f"you''r guess of { str(guess) } is bigger than the number try again.  \n")








 