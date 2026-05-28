#Karina
#Given an array of 12 random integers, find and print all "Peaks."
# A peak is defined as an element that is strictly greater than the neighbors immediately to its left and right.
import random
#Dataset with 12 numbers
dataset=[]
for i in range(12):
    dataset.append(random.randint(0,99))
print (dataset)

if dataset[0]>dataset[1]:
    print(f"Peak Detected: Value {dataset[0]} at index 0")
x=1

for i in range(10):
    if dataset[x]>dataset[x-1] and dataset[x]>dataset[x+1]:
        print(f"Peak Detected: Value {dataset[x]} at index {x}")
        x=x+1
if dataset[11]>dataset[10]:
        print(f"Peak Detected: Value {dataset[11]} at index 11")


