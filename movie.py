#Karina
#Movie theater
#Program checks age and determines what type of movie visitor can see

#Functions
#Main


def movie():
    age = int( input("Please enter your age: ") )
    if age >= 18:
        print ("You can see any movie including Rated-R")
    elif age >= 13:        #What does elif mean
        print ("You can see PG-13 movies")
    else: #Ends conditional statements
        print("You can see PG movies")
movie()

