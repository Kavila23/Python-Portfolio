#Karina

import webbrowser
#Init
url=["https://cdn.forevervacation.com/uploads/blog/thailand-visitor-guide-things-to-do-4406.jpg","https://delivery.gfobcontent.com/api/public/content/ac9edf5a49524b009609567ebc43040e?v=4159cf2e",
      "https://cdn.britannica.com/22/266122-050-DC806202/statue-Christ-the-Redeemer-Rio-de-Janiero-Brazil.jpg",
      "https://www.scenic.eu/-/media/project/scenic/scenic-tours/scenic-au/blog/3000-x-1500-header-banner/scl_swiss_alps_switzerland_001_3000x1500.jpg?h=1500&iar=0&w=3000&rev=6fa0c3152d1c4135bf9c3b600925df87&hash=FE0E0585BD739AB146CA6FB18B0F0B48"]

descriptions=["Thailand is a vibrant Southeast Asian kingdom renowned for its tropical beaches, decorated temples, and rich culture",
              "Morroco is a vibrant North African kingdom bordering the Atlantic and Mediterranean, known for its diverse landscapes—ranging from the Atlas Mountains to the Sahara Desert—and a rich, blended culture of Berber, Arab, and European influences",
              "Brazil is the largest country in South America and the fifth-largest in the world by area and population. It holds nearly 50% of the worlds remaining tropical forests.",
              "Switzerland is a landlocked, mountainous country in Central Europe known for its neutrality, stunning Alpine scenery, and high quality of life"]


print("Welcome to the vacation generator!")
weather=input("Do you want to go somewhere cold or hot? (cold, hot): ")
if weather=="cold":
    geography=input("Do you want to go somewhere mountainous or jungle-like? (mountains, jungle): ")
    if geography=="mountains":
       webbrowser.open("https://www.scenic.eu/-/media/project/scenic/scenic-tours/scenic-au/blog/3000-x-1500-header-banner/scl_swiss_alps_switzerland_001_3000x1500.jpg?h=1500&iar=0&w=3000&rev=6fa0c3152d1c4135bf9c3b600925df87&hash=FE0E0585BD739AB146CA6FB18B0F0B48")
       print(descriptions[3])
    elif geography=="jungle":
        webbrowser.open("https://cdn.forevervacation.com/uploads/blog/thailand-visitor-guide-things-to-do-4406.jpg")
        print(descriptions[0])
elif weather=="hot":
    continent=input("Do you want to go to Africa or Soouth America? (africa, south america): ")
    if continent=="africa":
        webbrowser.open("https://delivery.gfobcontent.com/api/public/content/ac9edf5a49524b009609567ebc43040e?v=4159cf2e")
        print(descriptions[1])

    elif continent=="south america":
        webbrowser.open("https://cdn.britannica.com/22/266122-050-DC806202/statue-Christ-the-Redeemer-Rio-de-Janiero-Brazil.jpg")
        print(descriptions[2])







#Sources of Information:
#Image: Picture of Thailand
#Author name: Jess Leak
#URL Website: https://forevervacation.com/the-vacationer/thailand-visitor-guide-things-to-do
#Article Name: Thailand Visitor Guide: Things To Do
#Date: 2024

#Image: Picture of Morocco
#Author name:N/A
#URL Website: https://www.cosmos.com/tour/highlights-of-morocco/6780/
#Article Name: Highlights of Morocco
#Date: N/A

#Image: Picture of Brazil
#Author name:N/A
#URL Website: https://www.britannica.com/place/Brazil
#Article Name: Brazil
#Date:3/2/26

#Image: Picture of Switzerland
#Author name: N/A
#URL Website: https://www.scenic.eu/blogs/the-allure-of-switzerland
#Article Name: The Allure of Switzerland
#Date: 3/4/25

