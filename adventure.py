#Adventure
#Create a program that takes users on a mini text adventure. Each choice leads to a new situation using nested if statement… Program must have 4 outcomes

def travel():
    print("Welcome to your traveling guide!")

    temp=input("Do you want to go somewhere cold or hot? (cold,hot):" )
    if temp=="hot":
        country = input("Do you want to go somewhere by an ocean? (yes,no): ")
        if country == "yes":
            print("The Bahamas!")
        elif country == "no":
            print("Mali!")

    else:
        country = input("Do you want to go somewhere by an ocean? (yes,no): ")
        if country =="yes":
            print("Sweden!")
        elif country == "no":
            print("Mongolia!")

travel()
