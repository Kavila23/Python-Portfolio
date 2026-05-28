#Karina Avila
#Tortaise and the Hare

import random

#🐢 The Tortoise
#🐇 The Hare


#Initital conditions
finish_line=50    #finish line
is_hare_asleep=False  #Hare starts awake
t_won=0
h_won=0

#the simulation loop
for i in range(100000):
    tortoise_pos = 0 #starting position
    hare_pos = 0 #starting position
    while tortoise_pos<finish_line and hare_pos<finish_line:
        # Tortoise always moves a short distance between 1 - 3 meters at random
        t_move=random.randint(1,3)
        if t_move==1:
            tortoise_pos=tortoise_pos+1
        elif t_move==2:
            tortoise_pos=tortoise_pos+2
        elif t_move==3:
            tortoise_pos=tortoise_pos+3


        # Hare has a 30% chance of falling a sleep for a turn
        h_sleep=random.randint(1,100)
        if h_sleep<=80:
            is_hare_asleep=True


        # If Hare is awake, it will move 1 - 10 meters at random
        elif h_sleep>=30:
            is_hare_asleep=False
            h_move=random.randint(1,10)
            hare_pos=hare_pos+h_move

        # Print the positions of the Hare and Tortoise after each round



    # Determine the winner
    if tortoise_pos >= finish_line:
        t_won=t_won+1

    else:
        h_won=h_won+1
print(f"🐢 The Tortoise won {t_won}")
print(f"🐇 The Hare won {h_won}")
