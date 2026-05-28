#Karina Avila
#Rock Paper Scissors
#A simulation of the popular rock paper scissors game where the players plays against the computer

#init
import random
print("Welcome to Rock...Paper...Scissors!")
win=0
lost=0
draw=0
#functions
def rps():
    global win
    global lost
    global draw
    while True:

        user = input("Do you want to chose rock, paper, or scissors? (rock, paper, scissors): ")
        computer=random.randint(1,3)
        if computer == 1 and user== "rock":
            print("The computer chose rock")
            print("Draw!")
            draw=draw+1
        elif computer == 2 and user == "paper":
            print ("The computer chose paper")
            print("Draw!")
            draw=draw+1
        elif computer == 3 and user == "scissors":
            print("The computer chose scissors")
            print("Draw!")
            draw=draw+1
        elif computer == 1 and user == "paper":
            print("The computer chose rock")
            print("You win!!")
            win=win+1
        elif computer== 1 and user == "scissors":
            print("The computer chose rock")
            print("You lost!")
            lost=lost+1
        elif computer == 2 and user == "rock":
            print ("The computer chose paper")
            print("You lost!")
            lost=lost+1
        elif computer == 2 and user=="scissors":
            print ("The computer chose paper")
            print("You win!!")
            win=win+1
        elif computer == 3 and user=="rock":
            print("The computer chose scissors")
            print("You win!!")
            win=win+1
        elif computer == 3 and user=="paper":
            print("The computer chose scissors")
            print("You lost!")
            lost=lost+1
        print(f"Win:{win}, Lost:{lost}, Draw:{draw}")
        again =input("Do you want to play again? (yes, no): ")
        if again=="no":
            print("Thanks for playing!!")
            break


#Main
rps()
