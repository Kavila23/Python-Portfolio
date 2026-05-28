#Karina Avila
import random

# 1. Setup the Game
secret_number=random.randint(1,100)
print(f"The Secret Number is: {secret_number}")


def linear_search():
    print("-Starting Linear Search Bot-")
    attempts=0
    for guess in range(1,101):
        if guess==secret_number:
            print(f"It took me {guess} times to guess {secret_number}!")
            break

def binary_search():
    low = 1
    high = 100
    found = False
    attempts=0
    while found == False:
        mid = (low+high)//2
        attempts=attempts+1
        if mid==secret_number:
            print(f"It took me {attempts} to find the secret number: {secret_number}")
            found=True
        elif mid < secret_number:
            low = mid + 1
        elif mid > secret_number:
            high = mid - 1






linear_search()
binary_search()
