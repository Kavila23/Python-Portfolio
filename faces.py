#Init
#Functions
#Convert takes in a message and returns the message with :) and :( converted to 🙂 and  🙁
def convert(msg):
    msg=msg.replace(":)", "🙂")

    msg=msg.replace(":(", "🙁")
    return msg

#Main takes in an input, then uses convert to print the input with emojis
def main():
    msg = input("Enter text: ")
    print( convert(msg) )



#Main
main()

