#Karina Avila
#Goal: Keep asking for a password until the user types "python".

def password():
    while True:
        pw=input("Please enter a password: ")
        if pw=="python":
            print("Correct!")
            break
        if pw != "python":
            print("Try again")

password()
