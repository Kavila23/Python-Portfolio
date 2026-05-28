#Escape Room

#Objective: Solve the challenges to succesfully escape the room!


#Initialization


import time
import random

inventory=[]
game_stats=[]


#functions
def intro():
    print("""Welcome to the Virtual Escape Room Thriller! The rules are simple:
    1) Select a theme of your choice
    2) Complete 1 challenge to get the key which will unlock the door.
    3) You get 5 tries, loose all of them? you loose the game.
    4) Play accuratley and wisely if you want to see the light of day!""")
    print("or else")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("....")

def menu():
    room=input("What theme would you like? (Jungle (j), Egypt (e), Robbery (r)): ")
    if room=="j":
        room_1()
    #elif room=="e":
    #else:


def room_1():
    pos_outcomes=["You hit a wall, wrong direction.", "The monster spat lava and you just stepped in it!", "NOO THE MONSTER CAUGHT YOU", "you fell into a dutch"]
    neg_outcomes=["you got the key!", "you gained berries"]
    print("""Welcome to room 1 mighty traveler. Escape the wild animals. Look out there is a bear heading your way!
    Use commands (forward,backward,left,right) to navigate to the key. Remember, each step is a risk,
    you do not know if you will loose lives or find the door to escape! AHHH ITS COMING BETTER HURRY UP!""")
    direction=input("Do you want to navigate forward, backward, left, or right? (forward, backward, left, right): " )
    while True:
        if direction== "left":
            result=random.choice(pos_outcomes and neg_outcomes)
            print(result)
        elif direction=="right":
            result=random.choice(pos_outcomes and neg_outcomes)
            print(result)
            #print("-1 life")
        elif direction=="forward":
            result=random.choice(pos_outcomes and neg_outcomes)
            print(result)
        elif direction=="backward":
            result=random.choice(pos_outcomes and neg_outcomes)
            print(result)
        else:
            break




intro()
menu()
