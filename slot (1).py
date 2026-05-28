#Karina and Evelyn
#Slot machine

import random

def game():
    print("""Welcome to the Slot Machine!
        Each spin costs 10 credits.""")

    symbols = ['7', '🌟', '💕', '✾', '🌟', '💕', '✾', '🌟', '💕', '✾']
    print (symbols)
    x = 0
    deposit = int(input("How much money do you want to deposit to start playing? (20) (50) (100): "))
    x = x + deposit
    while True:
        start = input("Press S to spin or Q to quit: (s) or (q): ")

        if start == 's':
            roll1 = random.choice(symbols)
            roll2 = random.choice(symbols)
            roll3 = random.choice(symbols)
            print("spinning...")
            print(roll1, roll2, roll3)
            if roll1 == '7' and roll2 == '7' and roll3 =='7':
                print("""Congrats you hit jackpot!
                    + 100 credits earned""")
                x = x + 100
            elif roll1 == roll2 == roll3:
                print("""Congrats! You won!
                    + 50 credits earned""")
                x = x + 50
            else:
                print("""Sorry no match this time.""")
            x = x - 10
            print(f"You have {x} credits")
            if x < 10:
                try:
                    add = int(input("You have insufficient funds. Please insert credits. (20) (50) (100): "))
                    x = x + add
                except:
                    print("Not an option")

        else:
            break

def test():
    x = 10000
    for i in range(1000):
        symbols = ['7', '🌟', '💕', '✾', '🌟', '💕', '✾', '🌟', '💕', '✾']
        roll1 = random.choice(symbols)
        roll2 = random.choice(symbols)
        roll3 = random.choice(symbols)
        print("spinning...")
        print(roll1, roll2, roll3)
        if roll1 == '7' and roll2 == '7' and roll3 =='7':
            print("""Congrats you hit jackpot!
                + 100 credits earned""")
            x = x + 1000
        elif roll1 == roll2 == roll3:
            print("""Congrats! You won!
                + 50 credits earned""")
            x = x + 50
        else:
            print("""Sorry no match this time.""")
        x = x - 10
    print(f"You have {x} credits")
    print(f"Casion won {10000 - x} credits")



game()
