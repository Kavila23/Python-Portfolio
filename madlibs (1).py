#Karina Avila
#To create a fun and interactive game that allows users to input words and generate a nonsensical story.
#init
#functions
import random




def madlibs():
    #Gather input
    name = ["Jake", "Alex", "Cindy", "Paul", "Carly", "Victoria"]
    food1= ["pizza", "hotdog", "burger", "pozole", "tamales", "fries", "Eggs"]
    food2= ["cake", "mochi", "banana", "strawberries", "sago", "blueberries"]
    noun1=["boot", "tire", "toilet", "cat", "dog", "house", "money"]

    Name=(input("Enter a Name: "))
    if Name=="random":
        Name=random.choice(name)

    Food1=(input("Enter a Food: "))
    if Food1=="random":
        Food1=random.choice(food1)

    Food2=(input("Enter a Food: "))
    if Food2=="random":
        Food2=random.choice(food2)

    Noun1=(input("Enter a Noun: "))
    if Noun1=="random":
        Noun1=random.choice(noun1)

    Place=(input("Enter a Noun: "))
    Number=(input("Enter a Number: "))
    Verb1=(input("Enter a Verb: "))
    Verb2=(input("Enter a Verb: "))
    Verb3=(input("Enter a Verb: "))


    #Story
    print(f"""I went on a roadtrip with  \033[1m{Name.upper()}\033[0m. We ate  \033[1m{Food1.upper()}\033[0m for lunch and  \033[1m{Food2.upper()}\033[0m for dessert.
We then went to the river and caught a  \033[1m{Noun1.upper()}\033[0m. We stayed in a \033[1m{Place.upper()}\033[0m next to the river.
We stayed there for  \033[1m{Number.upper()}\033[0m days. We  \033[1m{Verb1.upper()}\033[0m,  \033[1m{Verb2.upper()}\033[0m, and  \033[1m{Verb3.upper()}\033[0m the whole time because of how fun the trip was!""")

#Main
madlibs()
