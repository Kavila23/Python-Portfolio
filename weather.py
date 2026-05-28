#Karina Avila
#Weather
#Create a program that advises you on what clothing to wear and accessories to bring based on temperature given
#>=90
#>=70
#>=40
#39 and below

def weather():
    weather=int(input("Please enter weather: ") )
    if weather >=90:
        print("It will be extremely hot, so stay hydrated and wear sun block!")
    elif weather >=70:
        print("Wear shorts and well ventilated clothes")
    elif weather >=40:
        print("Wear a light jacket and/or sweater, it will be chilly")
    elif weather<39:
        print("Wear a thick jacket, gloves, hat, and scarf, its snowing!")
weather()
