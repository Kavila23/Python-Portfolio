#Karina
#secret
#Create the basic version of the game. The computer chooses a random number, and players guess until they get it right.

import random
secret = random.randint(1,5)
level= input("do you want to do the easy, medium, or hard mode? (easy, medium, hard): ")
while True:
    num=int(input("Please guess the secret number between 1 and 5: "))
    if num !=secret:
        if num==secret-1 or num == secret+1:
            print("Wrong number but your VERY hot!")
        if num==secret-2 or num == secret+2:
            print("Wrong number but your KINDA hot!")
        if num==secret-3 or num == secret+3:
            print("Wrong number but your warm!")
        if num==secret-4 or num == secret+4:
            print("Wrong number but your cold!")
        if num==secret-5 or num == secret+5:
            print("Wrong number but your SO cold!")
    elif num==secret:
        print("Correct! You win!")
        break
    check = input("Try again? (yes/no): ")
    if check=="yes":
        continue
    elif check =="no":
        break

