#Parity
#Karina Avila
#Create a program that prompts the user for a number and prints whether that number is even or odd.


#Init
#Functions
def main():
    num = int ( input("Please enter a number: ") )
    if is_even(num):
        print("EVEN")
    else:
        print("ODD")

#Main



def is_even(x):
    #Check if x is even
    if x % 2 == 0:
        return True
    else:
        return False
main()
