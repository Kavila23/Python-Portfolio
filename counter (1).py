#text is a string to be counted
#word counter takes in a string and prints how many words are in the string

def word_counter(text):
        #Your algorithm goes here
    x=text.split()
    print(x)
    y=len(x)
    print(y)



#Main
word_counter("This message has seven words in it")
word_counter("this is this is this is this is")
word_counter("f f f f f f f f f f f f f f f f f f f f f")
