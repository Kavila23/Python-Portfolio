#The purpose of my program is to match users to a Disney character based off their personality or their appearance




#init
import random
import time
import webbrowser


#arrays
names=['Cinderella', 'Carl Fredricksen from Up', 'Dr. Doofenshmirtz from Phineas and Ferb', 'Riley from Inside out','Aladdin from Aladdin', 'Hector from Coco', 'Rapunzel from Tangled']
skin=['fair', 'fair', 'light', 'light', 'dark', 'medium', 'fair']
hair=['medium', 'short', 'short', 'medium', 'short', 'short', 'long']
style=['elegant','elegant', 'casual', 'casual', 'traditional', 'traditional', 'elegant']
generation=['teenager', 'elderly', 'adult', 'child', 'adult', 'adult', 'adult']
social=['neutral', 'introvert', 'extrovert', 'neutral', 'extrovert', 'extrovert', 'neutral']
mood=['happy', 'sad', 'mad', 'happy', 'sad', 'sad', 'happy']
description=['Cinderella is an optimistic, kind-hearted princess who remains happy through her adversities.'
'She is both extroverted in ballroom dances and introverted as she remains calm and quiet.',
             'Carl Fredricksen is the 78-year-old, retired balloon salesman who transforms into a grumpy,'
             ' lonely widower following his wife Ellies death.',
              'Dr. Heinz Doofenshmirtz is a comically inept, German-accented mad scientist from '
              'Phineas and Ferb who seeks to rule the Tri-State Area.',
             'Originally a cheerful, hockey-loving girl from Minnesota, '
             'she struggles to adapt after moving to San Francisco. Her story focuses on emotional maturity,'
             ' guided by emotions in her mind, including Joy, Sadness, and later Anxiety.',
             'Aladdin is a charming, resourceful, and kind-hearted street urchin living in the Arabian city of Agrabah.'
             ' He survives with his monkey, Abu, before finding a magical lamp containing a genie.',
             'Hector is a charming, lanky, and forgotten skeleton in the Land of the Dead who seeks '
             'to return to the Land of the Living to see his daughter, Coco',
             'Rapunzel is the spirited, artistic, and adventurous protagonist. '
             'She is known for her 70-foot long, magical golden hair, which heals and reverses aging when she sings.']
url=["https://images2.minutemediacdn.com/image/upload/c_crop,w_4188,h_2355,x_0,y_350/v1763650928/images/voltaxMediaLibrary/mmsport/mentalfloss/01kagwjyz44th263y4ty.jpg"
     , "https://upload.wikimedia.org/wikipedia/en/9/9f/Carl_from_Up_2009.png", "https://upload.wikimedia.org/wikipedia/en/e/eb/Heinz_Doofenshmirtz.png",
     "https://static.wikia.nocookie.net/characters/images/1/19/Riley_Andersen_Render_from_Inside_Out_2.webp/revision/latest?cb=20240805063247",
       "https://upload.wikimedia.org/wikipedia/en/b/be/Aladdin_Disney_pose.png",
     "https://static.wikia.nocookie.net/pixar/images/1/1e/Coco_Hector_render.png/revision/latest/scale-to-width-down/1200?cb=20180901164229"
     , "https://static.wikia.nocookie.net/heroes-and-villain/images/d/da/Rapunzel_Render.png/revision/latest?cb=20250831231129"]

#functions

def personality():
    ask_emotion=input('How are you feeling today? (happy, sad, mad): ').lower().strip()
    if ask_emotion not in ['happy', 'sad', 'mad']:
        print("Not an option, try again")
        return


    if ask_emotion=="happy":
        ask_age=int(input('How old are you?: '))
        if ask_age>=13 and ask_age<18:
            ask_social=input('How social are you? (introvert, neutral, extrovert): ').lower().strip()
            if ask_social not in ['introvert', 'neutral', 'extrovert']:
                print("Not an option, try again")
                return

            if ask_social=="neutral":
                print('Skimming through recommendations...')
                for i in range(3):
                    print(3-i)
                    time.sleep(1)
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                result1=random.choice([names[0], names[6], names[3]])
                print(f'Got it!...Your Disney match is {result1}!')
                if result1==names[0]:
                    print(description[0])
                    webbrowser.open(url[0])
                elif result1==names[6]:
                    print(description[6])
                    webbrowser.open(url[6])
                elif result1==names[3]:
                    print(description[3])
                    webbrowser.open(url[3])
        else:
                print("Match Not Found")
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

    elif ask_emotion=="sad":
        ask_age=int(input('How old are you?: '))
        if ask_age>=18 and ask_age<65:
            ask_social=input('How social are you? (introvert, neutral, extrovert): ').lower().strip()
            if ask_social not in ['introvert', 'neutral', 'extrovert']:
                print("Not an option, try again")
                return
            if ask_social=="extrovert":
                print('Skimming through recommendations...')
                for i in range(3):
                    print(3-i)
                    time.sleep(1)
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                result2=random.choice([names[4], names[5]])
                print(f'Got it!...Your Disney match is {result2}!')
                if result2==names[4]:
                    print(description[4])
                    webbrowser.open(url[4])
                elif result2==names[5]:
                    print(description[5])
                    webbrowser.open(url[5])
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            else:
                print("Match not found")
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        else:
            print("Match not found")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

    elif ask_emotion=="mad":
        ask_age=int(input('How old are you?: '))
        if ask_age>=65:
            ask_social=input('How social are you? (introvert, neutral, extrovert): ').lower().strip()
            if ask_social not in ['introvert','neutral','extrovert']:
                print('Not an option, try again')
                return
            if ask_social=="introvert":
                print('Skimming through recommendations...')
                for i in range(3):
                    print(3-i)
                    time.sleep(1)
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                print(f'Got it!...Your Disney match is {names[1]}!')
                print(description[1])
                for i in range(3):
                    time.sleep(1)
                webbrowser.open(url[1])
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            else:
                print("Match Not Found")
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

        elif ask_age>=18 and ask_age<65:
            ask_social=input('How social are you? (introvert, neutral, extrovert): ').lower().strip()
            if ask_social not in ['introvert', 'neutral', 'extrovert']:
                print("Not an option, try again")
                return
            if ask_social=='extrovert':
                print('Skimming through recommendations...')
                for i in range(3):
                    print(3-i)
                    time.sleep(1)
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                print(f'Got it!...Your Disney match is {names[2]}!')
                print(description[2])
                webbrowser.open(url[2])
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            else:
                print("Match not found")
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        else:
            print("Match not found")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")




def appearance():
    ask_style=input('what is your style preference? (casual, traditional, elegant): ').lower().strip()
    if ask_style=='casual':
        ask_skin=input('What is your skin tone? (fair, light, medium, dark): ').lower().strip()
        if ask_skin not in ['fair','light','medium','dark']:
            print("Not an option, try again")
            return
        if ask_skin=='light':
            ask_hair=input("What is your hair length? (short, medium, long): ").lower().strip()
            if ask_hair not in ['short', 'medium', 'long']:
                print("Not an option, try again")
                return
            if ask_hair=="medium":
                print('Skimming through recommendations...')
                for i in range(3):
                    print(3-i)
                    time.sleep(1)
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                print(f'Got it!...Your Disney match is {names[3]}!')
                print(description[3])
                webbrowser.open(url[3])
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            elif ask_hair=="short":
                print('Skimming through recommendations...')
                for i in range(3):
                    print(3-i)
                    time.sleep(1)
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                print(f'Got it!...Your Disney match is {names[2]}!')
                print(description[2])
                webbrowser.open(url[2])
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            else:
                print("Match not found")
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

        else:
            print("Match not found")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

    elif ask_style=='elegant':
        ask_skin=input('What is your skin tone? (fair, light, medium, dark): ').lower().strip()
        if ask_skin not in ['fair','light','medium','dark']:
            print("Not an Option, Try Again")
            return
        if ask_skin=='fair':
            ask_hair=input("What is your hair length? (short, medium, long): ").lower().strip()
            if ask_skin not in ['short','medium','long']:
                print("Not an option, try again")
                return
            if ask_hair=="medium":
                print('Skimming through recommendations...')
                for i in range(3):
                    print(3-i)
                    time.sleep(1)
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                print(f'Got it!...Your Disney match is {names[0]}!')
                print(description[0])
                webbrowser.open(url[0])
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            elif ask_hair=="long":
                print('Skimming through recommendations...')
                for i in range(3):
                    print(3-i)
                    time.sleep(1)
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                print(f'Got it!...Your Disney match is {names[6]}!')
                print(description[6])
                webbrowser.open(url[6])
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            else:
                print("Match not found")
        elif ask_skin=='light':
            ask_hair=input("What is your hair length? (short, medium, long): ").lower().strip()
            if ask_hair not in ["short","medium","long"]:
                print("Not an option, try again")
                return
            if ask_hair=="short":
                print('Skimming through recommendations...')
                for i in range(3):
                    print(3-i)
                    time.sleep(1)
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                print(f'Got it!...Your Disney match is {names[1]}!')
                print(description[1])
                webbrowser.open(url[1])
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            else:
                print("Match not found")
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

        else:
            print("Match not found")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")


    elif ask_style=='traditional':
        ask_hair=input("What is your hair length? (short, medium, long): ").lower().strip()
        if ask_hair not in ['short', 'medium', 'long']:
            print("Not an option")
            return
        if ask_hair=="short":
            ask_skin=input('What is your skin tone? (fair, light, medium, dark): ').lower().strip()
            if ask_skin not in ['fair', 'light', 'medium', 'dark']:
                print("Not an option, try again")
                return
            if ask_skin=="medium":
                print('Skimming through recommendations...')
                for i in range(3):
                    print(3-i)
                    time.sleep(1)
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                print(f'Got it!...Your Disney match is {names[5]}!')
                print(description[5])
                webbrowser.open(url[5])
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            elif ask_skin=="dark":
                print('Skimming through recommendations...')
                for i in range(3):
                    print(3-i)
                    time.sleep(1)
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                print(f'Got it!...Your Disney match is {names[4]}!')
                print(description[4])
                webbrowser.open(url[4])
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            else:
                print("Match not found")
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

    else:
        print("Match not found")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")







def menu(choice):
    print("""Welcome to The Perfect Disney Match! The online quiz were you will be matched to a Disney character based
off your personality or appearance!""")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    while True:
        if choice=='personality':
            print('I see you have chosen to match a Disney character based on personality!')
            print('You will be redirected to the quiz in...')
            for i in range(3):
                print(3-i)
                time.sleep(1)
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            personality()
            ask_game=input("Do you want to continue playing or quit? (continue, quit): ").lower().strip()
            if ask_game=="quit":
                break


        elif choice=='appearance':
            print('I see you have chosen to match a Disney character based on appearance!')
            print('You will be redirected to the quiz in...')
            for i in range(3):
                print(3-i)
                time.sleep(1)
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            appearance()
            ask_game=input("Do you want to continue playing or quit? (continue, quit): ")
            if ask_game=="quit":
                break



menu('personality')




#---------------
# Sources of Images
#---------------
#Image 1: Picture of Cinderella
#Author name: Chelsea Thatcher
#URL Website: https://www.mentalfloss.com/entertainment/disney/cinderella-facts
#Article Name: 7 Magical Facts About ‘Cinderella’—From Deleted Scenes to Its Legacy
#Date: January 3, 2026

#Image 2: Picture of Carl Fredricksen
#URL Website: https://en.wikipedia.org/wiki/Carl_Fredricksen

#Image 3: Picture of Dr. Doofenshmirtz
#URL Website: https://en.wikipedia.org/wiki/Dr._Heinz_Doofenshmirtz

#Image 4: Picture of Riley
#URL Website: https://characters.fandom.com/wiki/Riley_Andersen

#Image 5: Picture of Aladdin
#URL Website: https://en.wikipedia.org/wiki/Aladdin_%28Disney_character%29

#Image 6: Picture of Hector
#URL Website: https://pixar.fandom.com/wiki/H%C3%A9ctor_Rivera

#Image 7: Picture of Rapunzel
#URL Website: https://heroes-and-villain.fandom.com/wiki/Rapunzel_(Disney)



