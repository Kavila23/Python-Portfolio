#Karina
#To-Do list
#Create the To-do List App that allows the user to keep track of items that must get done during the day.

def main():
    #Intro
    print("Hello! This is your online grocery list, you need to get the following:")
    groceries = ["strawberries", "milk", "blueberries", "oatmeal"]
    done=[]
    print(groceries)

    #1. Add an item to the to-do list

    add = input("Would you like to add to the grocery list? (yes/no): ")
    if add=="yes":
        add=input("What item would would you like to add to the list? ")
        groceries.append(add)
        print(groceries)
    elif add=="no":
        print(groceries)
    else:
        print("Not an option")
        print(groceries)

    #2. Remove an item or Clear the List

    delete=input("Would you like to remove from the grocery list? or do you want to clear the entire list? (remove, clear): ")
    if delete=="clear":
        groceries.clear()
        print(groceries)
        quit()
    elif delete=="remove":
        delete=input("What item would you like to remove? ")
        try:
            groceries.remove(delete)
        except:
            print("Item not in list")
        print(groceries)
    else:
        print("Not an option")
        print(groceries)


    # 3. Mark an item as Done

    completed=input("Do you want to mark something as done? (yes/no): ")
    if completed=="yes":
        completed=input("What item would you like to mark as done? ")
        try:
            groceries.remove(completed)
            done.append(completed)
            print(groceries)
            print(done)
        except:
            print("Item not in list")
            print(groceries)

    elif completed=="no":
        print("Okay bye!")
        exit
    else:
        print("Not an option")
        print(groceries)


main()
