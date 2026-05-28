#Karina
#Analyze the data, and unravel the story that the data is showing us.
#Do not look at the data, instead use code to find the answers

import pandas as pd

data = pd.read_csv('influencer.csv')

month=data['Month'].tolist()
views=data['Views'].tolist()
dislikes=data['Dislikes'].tolist()
subscriber=data['Subscriber(+-)'].tolist()
revenue=data['Revenue'].tolist()
filter=[]

def problem1(watch):
    for i in range(len(views)):
        if views[i]<= watch:
            filter.append([i])
    print(filter)
    filter.clear()


def problem2(growth):
    for i in range(len(subscriber)):
        if subscriber[i] >= growth:
            filter.append([i])
    print(filter)
    filter.clear()

def problem3(leak):
    for i in range(len(revenue)):
        if revenue[i]==leak:
            filter.append([i])
    print(filter)
    filter.clear()



problem1(2000)
print(data.loc[0:10])

problem2(50000)
print(data.loc[64:72])

problem3(0)
print(data.loc[98])
print(data.loc[107])


