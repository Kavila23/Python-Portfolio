#Karina
#Largest
#Write a function with 3 integer parameters (a,b,c) that prints the largest of the three numbers

#Functions
def largest (a, b, c): #abc are integers
    #Solutions goes here
    if a>b and b>c:
        print (a)
    elif b>a and a>c:
        print(b)
    else:
        print(c)


#Main
largest(1, 2, 3) #Sample Call
largest(20, 100, 10)#Sample call
largest (100, 50, 1) #Sample Call

