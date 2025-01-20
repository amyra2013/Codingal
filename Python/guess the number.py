import random
listofattempts=[]
def repeat():
    print('Hello! Welcome to the game of guesses!')
    name=input('Enter your name!')
    print("Hey {}!".format(name)) 
def show_hs():
    if len(listofattempts)==0:
        print("There's no high score as of now, it's yours for the taking!")
    else:
        print("The game's champion took just",min(listofattempts),"attempts to win.")
def start_game():
    attempts=0
    randominteger=int(random.randint(1,10))
    sq=input('Would you like to play a guessing game?')
    if sq.lower()=="yes":
        print("All right! Let's get started! \nThe rules are simple. The computer will choose a random number(from 1 to 10), and you will try to guess it. The game ends when you guess the correct answer.")
        repeat()
        show_hs()
    else:
        print("That's alright. Have a good day!")
        return

    while sq.lower()=="yes":
        try:
            inp=(int(input("Guess the number from 1-10 that the computer has chosen.")))
            if inp==randominteger:
                print("Congrats!You win!")
                attempts=attempts+1
                listofattempts.append(attempts)
                playagain=input('Wanna play again?')
                if playagain.lower()=="yes":
                    start_game()
                elif playagain.lower()=="no":
                     break
            elif inp <=1 or inp >10:
                print("Please enter a valid number.")
                attempts=attempts+1
                raise ValueError("Please enter a number that has the following characteristics:\n 1) Is not larger than 10 or smaller than 1. \n2) Must be a whole number.")
            elif inp <randominteger:
                attempts=attempts+1
                print("The number is lower than what you guessed! Try again.")
                inp=(int(input("Guess the number from 1-10 that the computer has chosen.")))
            elif inp >randominteger:
                 attempts=attempts+1
                 print("The number is higher than what you guessed! Try again.")
                 inp=(int(input("Guess the number from 1-10 that the computer has chosen.")))
        except ValueError as err:
            print("Oh, that isn't a valid statement. Try again!")
            print(err)
            

show_hs()
start_game()



