#Karina Avila
#This program takes in a number as a parameter or as input from the user and prints every even number up to the given number.
def even():
    num = int(input("Enter an even number: "))
    for i in range(2,num+1, 2):
        print(i)
even()
