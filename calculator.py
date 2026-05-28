#Calculator
#Create a program that prompts users to enter two numbers, an operator, and prints the result of the operation

#Init
#Functions
def main():
    #Welcome the user
    print("Welcome to the Simple Calculator!")
    #Collect your input
    num1=int(input("Enter a number: "))
    num2=int(input("Enter another number: "))
    operator=input("Enter an operation symbol: ")
    #Perform the operation
    if operator == "+":
        print(calc_sum(num1, num2))
    if operator == "-":
        print(calc_sub(num1, num2))
    if operator == "*":
        print(calc_multi(num1, num2))
    if operator == "/":
        print(calc_div(num1, num2))

#This function returns the sum of x and y
def calc_sum(x,y):             #how do u know x and y are variables for num1 and num2
    return x + y  #or total=x+y ,and then next line, renturn total
def calc_sub(x,y):
    return x - y
def calc_multi(x,y):
    return x * y
def calc_div(x,y):
    return x / y



#Main
print(calc_sum(23,89))
main()
