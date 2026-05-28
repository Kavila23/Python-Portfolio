#Nickname
#Create a program that asks the user 3 questions before revealing a “nickname” for the user. Program must have 8 outcomes

def animal():
    print ("Welcome to the Animal Nickname Quiz!")
    personality=input("Are you an introvert or extrovert? (introvert,extrovert): " )
    if personality=="introvert":
        emotion = input("Are you more lazy or patient? (lazy,patient): ")
        if emotion == "lazy":
            feeling=input("Are you more anxious or quiet? (anxious, quiet): ")
            if feeling=="anxious":
                print("Sloth!")
            elif feeling=="quiet":
                print("Turtle!")
        elif emotion=="patient":           #can u add a elif or else inside a if statement?  #can u use a variable 2 times named the same thing but has different meanings?
            caring=input("Are you more careless or considerate? (careless, considerate): ")
            if caring=="careless":
                print("Owl!")
            elif caring=="considerate":
                print("Deer!")

    if personality=="extrovert":
        focus=input("Are you more distracted or attentive? (distracted, attentive): ")
        if focus=="distracted":
            pace=input("Are you fast-paced or slow-paced? (fast-paced, slow-paced): ")
            if pace=="fast-paced":
                print("Squirrel!")
            elif pace=="slow-paced":
                print("Capybara!")
        elif focus=="attentive":
            lifestyle=input("Are you more domestic or adventurous? (domestic, adventurous): ")
            if lifestyle=="domestic":
                print("Dog!")
            elif lifestyle=="adventurous":
                print("Dolphin!")
animal()
