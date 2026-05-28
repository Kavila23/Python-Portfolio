#karina
#Goal: Create a global variable balance

#initialize
money=0

#functions
def withdraw():
    #Allows you to withdraw money to account
    global money
    withdraw=int(input("how much money would you like to withdraw?: "))
    money=money-withdraw
    print(f"Withdrew {withdraw}")
def deposit():
    #Allows you to deposit money to account
    global money
    deposit=int(input("how much money would you like to deposit?: "))
    money=money+deposit
    print(f"Deposited {deposit}")
def display_total():
    #prints your current balance
    global money
    print(f"Balance = {money}")
#Main
deposit()
withdraw()
display_total()
