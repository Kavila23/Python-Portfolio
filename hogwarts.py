#Karina
#program that prompts the user for their name and simulates being assigned one of the 4 hogwarts houses

#Initialize
import time
import random

#Functions
def main():
    print("Welcome to Hogwarts")
    name = input("What is your name: ")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("....")
    print( house(name) )


#This function checks a name and returns a house from harry potter
def house(name):
    if name == "Harry" or name == "Ron" or name == "Hermione":
        return "Gryffindor!"
    elif name == "Newt" or name== "Nymphadora" or name== "Pomona":
        return "Hufflepuff!"
    elif name=="Luna" or name== "Cho" or name== "Filius":
        return "Ravenclaw!"
    elif name =="Voldemort" or name== "Draco" or name== "Severus":
        return "Slytherin!"
    else:
        roll = random.randint(1,4)
        if roll==1:
            return "Gryffindor!"
        elif roll==2:
            return "Hufflepuff!"
        elif roll==3:
            return "Ravenclaw!"
        elif roll == 4:
            return "Slytherin!"




#Main
main()
