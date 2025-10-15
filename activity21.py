import random

print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++")
print("\nNumber Guessing Game, 1 to 10")
print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++")

random_value = random.randint(1,10)
tries = 0
continue_game = True

name = input("What is your name? --> ")

while continue_game == True:
    num = eval(input("Enter a number between 1 and 10 --> "))   
    tries += 1
    if num == random_value:
        print(f"YOU WON!!~... weak. It took you {tries} tries")
        break
    else:
        print("AHHAHAHAHAHA NOT EVEN CLOSE BABY!!")
        continue    

print(f"{name}, Nice took you long enough")