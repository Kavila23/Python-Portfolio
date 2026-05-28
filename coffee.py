#Coffee
#Students ask the user a few questions about performances (sweet, hot/cold, caffeine, etc.) and "recommend" a drink.
def coffee():
    print("Welcome to Python Cafe!")

    #Collect 1st input from user
    temp = input("Do you want something hot or cold? (hot,cold):")

    #Hot recommendation
    if temp == "hot":
        sweet = input("Do you want something sweet? (yes,no): ")
    #Sweet recommendation
        if sweet == "yes":
            print("Hot Chocolate!")
        elif sweet == "no":
            print("Black Coffee!")

    else:
        sweet = input("Do you want something sweet? (yes,no): ")
        if sweet =="yes":
            print("Iced Latte!")
        elif sweet == "no":
            print("Cold Brew!")

coffee()
