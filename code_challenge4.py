print("Welcome to Manhwa Recommender!")
print("Pick a genre:")
print("1. Action")
print("2. Romance")
print("3. Comedy")

genre = input("Type the genre you want: ").lower()

if genre == "action":
    print("You have chosen the Action genre.")
    duration = input("Duration of manhwa (Short, Medium, Long): ").lower()

    if duration == "short":
        decade = input("Select decade (2010/2020): ")
        if decade == "2010":
            print("Short Action Manhwa (2010): \nThe Breaker \nAbility")
        elif decade == "2020":
            print("Short Action Manhwa (2020): \nMercenary Enrollment \nLeviathan")
        else:
            print("Invalid decade.")
    
    elif duration == "medium":
        decade = input("Select decade (2010/2020): ")
        if decade == "2010":
            print("Medium Action Manhwa (2010): \nGirls of the Wild’s \nNoblesse")
        elif decade == "2020":
            print("Medium Action Manhwa (2020): \nSolo Leveling \nWeak Hero")
        else:
            print("Invalid decade.")

    elif duration == "long":
        decade = input("Select decade (2010/2020): ")
        if decade == "2010":
            print("Long Action Manhwa (2010): \nTower of God \nThe God of High School")
        elif decade == "2020":
            print("Long Action Manhwa (2020): \nEleceed \nNano Machine")
        else:
            print("Invalid decade.")
    else:
        print("Invalid duration.")

elif genre == "romance":
    print("You have chosen the Romance genre.")
    duration = input("Duration of manhwa (Short, Medium, Long): ").lower()

    if duration == "short":
        decade = input("Select decade (2010/2020): ")
        if decade == "2010":
            print("Short Romance Manhwa (2010): \nOrange Marmalade \nMy Dear Cold-Blooded King")
        elif decade == "2020":
            print("Short Romance Manhwa (2020): \nSeasons of Blossom \nDaytime Star")
        else:
            print("Invalid decade.")
    
    elif duration == "medium":
        decade = input("Select decade (2010/2020): ")
        if decade == "2010":
            print("Medium Romance Manhwa (2010): \nSomething About Us \nHe is a High School Girl")
        elif decade == "2020":
            print("Medium Romance Manhwa (2020): \nA Business Proposal \nOperation: True Love")
        else:
            print("Invalid decade.")

    elif duration == "long":
        decade = input("Select decade (2010/2020): ")
        if decade == "2010":
            print("Long Romance Manhwa (2010): \nCheese in the Trap \nUnTouchable")
        elif decade == "2020":
            print("Long Romance Manhwa (2020): \nWhat's Wrong with Secretary Kim? \nPositively Yours")
        else:
            print("Invalid decade.")
    else:
        print("Invalid duration.")

elif genre == "comedy":
    print("You have chosen the Comedy genre.")
    duration = input("Duration of manhwa (Short, Medium, Long): ").lower()

    if duration == "short":
        decade = input("Select decade (2010/2020): ")
        if decade == "2010":
            print("Short Comedy Manhwa (2010): \nThe Sound of Your Heart \nThe Friendly Winter")
        elif decade == "2020":
            print("Short Comedy Manhwa (2020): \nHow to Fight \nStudy Group")
        else:
            print("Invalid decade.")
    
    elif duration == "medium":
        decade = input("Select decade (2010/2020): ")
        if decade == "2010":
            print("Medium Comedy Manhwa (2010): \nYumi’s Cells \nGirls of the Wild’s")
        elif decade == "2020":
            print("Medium Comedy Manhwa (2020): \nOmniscient Reader’s Viewpoint \nThe Boxer (Comedy Elements)")
        else:
            print("Invalid decade.")

    elif duration == "long":
        decade = input("Select decade (2010/2020): ")
        if decade == "2010":
            print("Long Comedy Manhwa (2010): \nGod of Bath \nThe Gamer")
        elif decade == "2020":
            print("Long Comedy Manhwa (2020): \nLookism \nManager Kim")
        else:
            print("Invalid decade.")
    else:
        print("Invalid duration.")

else:
    print("Invalid genre. Please pick Action, Romance, or Comedy.")
