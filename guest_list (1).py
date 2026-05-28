#Karina Avila
#Guest List


guests = ["Alice", "Bob", "Charlie", "David", "Eve",
"Frank", "Grace", "Heidi", "Ivan", "Judy",
"Kevin", "Liam", "Mallory", "Nia", "Oscar",
"Peggy", "Quinn", "Riley", "Sybil", "Trent",
"Uma", "Victor", "Walter", "Xander", "Yara",
"Zane", "Amari", "Blake", "Casey", "Dakota"]
name=input("What is your friend's name, Bob?  ")
guests.append(name)
vip=input("What is the VIP's name?  ")
guests.insert(0,vip)
new=input("What is the name of the new person?  ")
guests[4]=new
print(len(guests))
print(guests)
