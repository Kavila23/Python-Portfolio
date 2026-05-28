#Create a Python program that generates and prints out the lyrics to the song "99 Bottles of Milk on the Wall."

def bottles():
    x = 100
    for i in range(100):
        if x==1:
            print("1 bottle of milk on the wall, 1 bottle of milk, Take one down pass it around, 1 bottle of milk on the wall")
            print("No more bottles of milk on the wall, Boo Hoo!")
        else:
            print(f"{x} bottles of milk on the wall, {x} bottles of milk, Take one down pass it around, {x-1} bottles of milk on the wall")
            x=x-1
bottles()
