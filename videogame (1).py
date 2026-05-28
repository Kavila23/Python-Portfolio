#Karina
#A new indie game  just received feedback on their beta test. You have the data and need to analyze it to see where the team could make improvements.

import pandas as pd

data = pd.read_csv('gamedev.csv')

level=data['Level'].tolist()
time=data['Time'].tolist()
rating=data['Rating'].tolist()
summary=data['Summary'].tolist()
feedback=data['Feedback'].tolist()
filter=[]

#Print a specific row from the dataframe
print(data.loc[3]) #loc is short for location


def find_problems1():
    #STEP ONE: CREATE THE LOOP
    for i in range(len(rating)):
        #Step Two: THE CONDITIONAL STATEMENT
        if rating[i]<2:
            #STEP THREE: ADD ITEM TO FILTER
            filter.append([i])
    #STEP FOUR: PRINT RESULTS AND CLEAR
    print(filter)
    filter.clear()

def find_problems2(times):
    #STEP ONE: CREATE THE LOOP
    for i in range(len(time)):
        #Step Two: THE CONDITIONAL STATEMENT
        if time[i]>times:
            #STEP THREE: ADD ITEM TO FILTER
            filter.append([i])
    #STEP FOUR: PRINT RESULTS AND CLEAR
    print(filter)
    filter.clear()

def find_problems3(leak):
    #STEP ONE: CREATE THE LOOP
    for i in range(len(feedback)):
        #Step Two: THE CONDITIONAL STATEMENT
        if leak in feedback[i]:
            #STEP THREE: ADD ITEM TO FILTER
            filter.append([i])
    #STEP FOUR: PRINT RESULTS AND CLEAR
    print(filter)
    filter.clear()



#main
find_problems1()
print(data.loc[[14,34,77]])#When u have multiple #'s you use double brackets

find_problems2(400)
print(data.loc[79])

find_problems3("secret")
print(data.loc[66])
