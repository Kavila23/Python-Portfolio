#initialize
score = 0

#Functions
def add_onehundred():
    global score
    score = score + 100
    print(f"You've earned 100 points!")
#main
add_onehundred()
add_onehundred()
add_onehundred()
print(f"Total score = {score}")
