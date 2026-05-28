#Karina
#Grade
#Write a function that asks the user to input a score as an integer and returns the appropriate letter grade (90+ = A, 80+ = B, etc)

def grades():
    score=int(input("Please enter your score: "))
    if score >=90:
        print ("A")


    elif score >=80:
        print ("B")


    if score <=79 and score>=70:     #if u start with if and elif do u have to continue with else? no
        print("C")

    if score <=69 and score >=60:
        print("D")
    elif score <=59:
        print ("F")

#Main
grades()
