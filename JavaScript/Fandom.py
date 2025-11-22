Fandom=int(input('Enter the number of your favourite fan universe:1 for Harry Potter, 2 for PJO/HOO/TOA/Kane Chronicles/Magnus Chase, 3 for The Hunger Games'))
if Fandom==1:
    house=int(input('Enter your house, Potterhead, and welcome to Hogwarts: 1.Gryffindor, where dwell the brave at heart. 2.Slytherin, a house of cunning and resourcefulness. 3.Ravenclaw,a house of intelligence and creativity. 4.Hufflepuff, a house industrious perseverance and people who never give up!'))
    if house==1:
        print("Hello, Gryffindor! You're in some pretty good company: the likes of Harry Potter, Hermione Granger, the Weasleys, and Neville Longbottom!")
        if house==2:
            print("Hey there, cunning Slytherin! You've got to have some rather...devious friends: Draco Malfoy, Vincent Crabbe, Gregory Goyle, and Pansy Parkinson might just be among your top picks!")
            if house==3:
                print("Greetings, bright Ravenclaw! You're surrounded by geniuses and top-hole wizards like Luna Lovegood, Cho Chang, and Rowena Ravenclaw!")
                if house==4:
                    print("Hi, Hufflepuff! You have some extremely kind and self-sacrificing companions, including Cedric Diggory!")
elif Fandom==2:
    parent=int(input("Hey, half-blood! Who's your godly parent?(1.Athena 2.Dionysus 3.Poseidon 4.Aphrodite 5.Hephaestus 6.Apollo)"))
    if parent==1:
        print("A child of Athena, eh? You're one among many great thinkers and strategists, including Annabeth Chase and Malcolm Pace.")
    elif parent==2:
        print("Wow, a child of Dionysus! You must really love parties!")
    elif parent==3:
        print('As a child of Poseidon, you, like the sea, probably do not enjoy being restrained!*wink*')
    elif parent==4:
        print("Greetings, charming child of Aphrodite!")
    elif parent==5:
        print("Good day. You, as a child of Hephaestus the blacksmith god, probably know how to fix anything...even death and a broken metal dragon!")
    elif parent==6:
        print("Hello, bright child of Apollo! How's your dad doing? Did you hear about his latest sojourn into the mortal world? It makes a pretty good story!")
elif Fandom==3:
    print("Welcome, tribute, to the Hunger Games!")
    district=int(input('Type 1 if you are from the Capitol, 2 for District 1/2/4, 3 for Districts 3/5/6/7/8/9/10, 4 for District 11, 5 for District 12 (or type 6 for a surprise)'))
    if district==1:
        print('You, as a resident of the Capitol, have probabbly enjoyed untold pleasures as rebel teenagers fought to the death for your entertainment. Entitlement personified!')
    elif district==2:
        print('From District 1/2/4, you doubtless underwent Career training to win in case you were reaped for the Games, but also nevertheless enjoyed almos Capitol-like pleasures.')
    elif district==3:
        print('From District 3/5/6/7/8/9/10,you probably grew up among people who were poorly treated and unhappy with their lives, so when Katniss Everdeen, the Mockingjay, entered the scene, you probably jumped at the chance to do something and led a revolt against the Capitol. Maybe you hold an important leadership position today! ')
    elif district==4:
        print('District 11, the rigidly governed farming district, was your home. You probably grew up in a strict setting,watching friends die at the hands of Peacekeepers, so, when the rebellion began, you, too, probably helped Katniss fuel the fire against the Capitol.')
    elif district==5:
        print('District 12, the once-lowly district whose tributes had no standing in the Games...until the Mockingjay. You were one of many who led the revolt against the rule of the Capitol, inspired by Katniss and Peeta.')
    elif district==6:
        print('Ooh, District 13! You were one of the strictly controlled residents of the undreground bunkers governed by Coin, who later sheltered Katniss Everdeen from the Capitol')
    else:
        print('Sorry, not a valid district.')
else:
    print('Sorry, not a valid fandom.')

