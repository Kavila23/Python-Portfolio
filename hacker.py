#Karina

import pandas as pd

data= pd.read_csv('hacker.csv')


log_id=data['Log_ID'].tolist()
ip_address=data['IP_Address'].tolist()
protocol=data['Protocol'].tolist()
data_kb=data['Data_KB'].tolist()
time=data['Time'].tolist()
description=data['Description'].tolist()
filter=[]



def problem1(leak):
    for i in range(len(description)):
        if leak in description[i]:
            filter.append([i])
    print(filter)
    filter.clear()


def problem2(stole):
    for i in range(len(data_kb)):
        if data_kb[i]>=stole:
            filter.append([i])
    print(filter)
    filter.clear()

def problem3(reset):
    for i in range(len(description)):
        if reset in description[i]:
            filter.append([i])
    print(filter)
    filter.clear()


problem1("Failed")
print(data.loc[193:195])

problem2(5000)
print(data.loc[199])

problem3("Reset")
print(data.loc[[204,205,207,210,214,218,221,222,224,231,235]])
