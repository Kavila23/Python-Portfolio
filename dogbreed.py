#Karina Avila
#Dog Breed (Create Task)
#The purpose of my program is to help users choose a dog breed that meets their needs


#init
import pandas as pd
data= pd.read_csv('dogs.csv')
import random

min_weight=data['Minimum Weight'].tolist()
max_weight=data['Maximum Weight'].tolist()
name=data['Name'].tolist()
temp=data['Temperament'].tolist()
image=data['Image'].tolist()
bred=data['BredFor'].tolist()
tiny=[]
small=[]
medium=[]
large=[]
picture=[]
mood=[]
want=[]


#functions
def getDogSize(size):
    for i in range(len(name)):
        if size =='tiny':
            if max_weight[i]<=10:
                tiny.append(name[i])
        elif size=='small':
            if max_weight[i]<=25 and max_weight[i]>=11:
                small.append(name[i])
        elif size=='medium':
            if max_weight[i]<=60 and max_weight[i]>=26:
                medium.append(name[i])
        else:
            if max_weight[i]>=60:
                large.append(name[i])
    if size=='tiny':
        rec1=random.choice(tiny)
        print(f'I recommend a {rec1}')
    if size=='small':
        rec2=random.choice(small)
        print(f'I reccomend a {rec2}')
    if size=='medium':
        rec3=random.choice(medium)
        print(f'I recommend a {rec3}')
    if size=='large':
        rec4=random.choice(large)
        print(f'I recommend a {rec4}')


def info(breed_name):
    for i in range(len(name)):
        if breed_name==name[i]:
            print(name[i])
            picture.append(image[i])
            print(picture)
            mood.append(temp[i])
            print(f"Here is the temperance of the {breed_name}: {mood}")
    if picture==[]:
        print(f"{breed_name} not found")

def breeding(purpose):
    for i in range(len(name)):
        if purpose in bred[i]:
            want.append(name[i])
    print(f"Heres a list of dog breeds that partain to {purpose}: {want}")
    rec=random.choice(want)
    print(f'I recommend a {rec}')
    if want==[]:
        print(f"{purpose} not found")

def menu():
    print("Welcome to Find your Perfect Dog!")
    while True:
        find=input("what would you like to look for: size, behavior, purpose, or exit? :")
        if find=="size":
            ask_size=input("Would you like a tiny, small, medium, or large dog? ")
            if ask_size=="tiny":
                getDogSize("tiny")
            elif ask_size=="small":
                getDogSize("small")
            elif ask_size=="medium":
                getDogSize("medium")
            else:
                getDogSize("large")

        elif find =="behavior":
            ask_name=input("Enter a dog name to find their behavior: ")
            info(ask_name)
        elif find == "purpose":
            ask_purpose=input("Enter what you want the dog for: ")
            breeding(ask_purpose)
        else:
            break


















menu()
#getDogSize('tiny')
#getDogSize('small')
#getDogSize('medium')
#getDogSize('large')
#info('Chinook')
#breeding('Lapdog')



#Sources
#Dog Dataset
#Website Name: Code.org
#URL: https://code.org/en-US
#Dataset Source:https://thedogapi.com/en

