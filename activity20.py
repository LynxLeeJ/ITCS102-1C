
print("Would you like to wash?")

Clothes = True

while Clothes == True:
     wash_again = input("Continue (yes/no) --> ")
     if wash_again == "yes":
          print("Washing it again ...")
          continue
     else:
        print("Washing has stopped ...")
        break
    
    