name = (input("Hi, What is your name? -->  "))
print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++")
print("\nODD NUMBER SELECTOR, press 0 to stop the loop")
print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++")

sum = 0
number = True
odd = ""
while number == True:
    num = eval(input("Enter an number --> "))

    if num %2 == 1:
        print(f"{num} is an odd number")
        odd = odd + str(num) + " "
        sum = sum + num
        continue
    else:
        if num == 0:
            print(f"\nHello Mr/Ms {name}")
            print(f"The odd numbers you entered are {odd}")
            print(f"The sum of the odd numbers you entered is {sum}")
            break
        else:
            print(f"{num} is not an odd number, try again")
            continue
        print(terminated)


         

