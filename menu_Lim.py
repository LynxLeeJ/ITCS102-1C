import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# uses print for UI , variables (choice), while loop (repeats), try/except (error handling).
def main_menu():
    while True:
        clear()
        print("===================================================")
        print(" PYTHON FUNDAMENTALS - TEXT-BASED INTERACTIVE MENU ")
        print("===================================================")
        print("\n\t1 - Print Statements")
        print("\t2 - Variables")
        print("\t3 - Operators")
        print("\t4 - Conditionals")
        print("\t5 - Loops")
        print("\t6 - Lists")
        print("\t7 - Functions")
        print("\t8 - Run Your Own Python Code")
        print("\t0 - Exit Program")
        print("\n===========================================")

        try:
            choice = int(input("Enter your choice: "))   # try/except prevents crash\makes you dont run the code again
        except:
            print("Invalid input. Please enter numbers only \n\t\t\t(0-8).")
            continue

        if choice == 0:
            print("Goodbye!")
            break
        
        elif choice == 1:
            printfirstchoice()
        elif choice == 2:
            variablessecondchoice()
        elif choice == 3:
            operatorsthirdchoice()
        elif choice == 4:
            conditionalsfourthchoice()
        elif choice == 5:
            loopsfifthchoice()
        elif choice == 6:
            listssixchoice()
        elif choice == 7:
            functionsseventhchoice()
        elif choice == 8:
            usereighthchoice()
        else:
            print("Invalid choice.")


def printfirstchoice():
    while True:
        clear()
        print("\n---------------'' PRINT STATEMENTS ''---------------")
        print("\t1 - Demo")
        print("\t2 - Explanation")
        print("\t0 - Back")
        print("\n----------------------------------------------------")

        try:
            choice = int(input("Enter choice: "))
        except:
            print("Please put the desired choice.")
            continue

        if choice == 0:
            return

        elif choice == 1:
            # DEMO
            clear()
            print("DEMO: print() shows text or values on the screen.")
            print("\nExample: print('Hello, World!')")
            print("\nOutput: Hello, World!")
            print()
            input("Press Enter...")

        elif choice == 2:
            # DETAILED EXPLANATION
            clear()
            print("PRINT EXPLANATION:")
            print("- print() displays text or values.")
            print("\n- You can print numbers, strings, and variables.")
            print("\n- Example: print('Sum:', 2 + 3) prints Sum: 5.")
            print("\n- f-strings allow combining text and variables.")
            print()
            input("Press Enter...")


# ---------------- VARIABLES MENU ----------------
def variablessecondchoice():
    while True:
        clear()
        print("\n--------------- VARIABLES ---------------")
        print("\t1 - Demo")
        print("\t2 - Explanation")
        print("\t0 - Back")
        print("\n-----------------------------------------")

        try:
            choice = int(input("Enter choice: "))
        except:
            print("Numbers only.")
            continue

        if choice == 0:
            return

        elif choice == 1:
            clear()
            
            x = 10
            name = "Python"
            print("x =", x)
            print("name =", name)
            print()
            input("Press Enter...")

        elif choice == 2:
            clear()
            print("VARIABLES EXPLANATION:")
            print("- Variables store data such as numbers or text.")
            print("\n- Example: age = 18 saves 18 inside the name 'age'.")
            print("\n- You can print variables or use them in operations.")
            print()
            input("Press Enter...")


def operatorsthirdchoice():
    while True:
        clear()
        print("\n--------------- OPERATORS ---------------")
        print("\t1 - Demo")
        print("\t2 - Explanation")
        print("\t0 - Back")
        print("\n-----------------------------------------")

        try:
            choice = int(input("Enter choice: "))
        except:
            print("Numbers only.")
            continue

        if choice == 0:
            return

        elif choice == 1:
            clear()
            a = 5
            b = 3
            print("a =", a, "b =", b)
            print("a + b =", a + b)  # operator
            print("a * b =", a * b)
            print("a > b =", a > b)  # comparison operator
            print()
            input("Press Enter...")

        elif choice == 2:
            clear()
            print("OPERATORS EXPLANATION:")
            print("\n- Arithmetic: +  -  *  /  %")
            print("\n- Comparison: ==  !=  >  <")
            print("\n- Operators let Python do math or compare values.")
            print()
            input("Press Enter...")


def conditionalsfourthchoice():
    while True:
        clear()
        print("\n--------------- CONDITIONALS ---------------")
        print("\t1 - Demo")
        print("\t2 - Explanation")
        print("\t0 - Back")
        print("\n--------------------------------------------")

        try:
            choice = int(input("Enter choice: "))
        except:
            print("Numbers only.")
            continue

        if choice == 0:
            return

        elif choice == 1:
            clear()
            num = 10
            if num > 5:
                print("10 is greater than 5")
            else:
                print("10 is not greater")
            print()
            input("Press Enter...")

        elif choice == 2:
            clear()
            print("CONDITIONALS EXPLANATION:")
            print("\n\t- if, elif, else allow your code to make decisions.")
            print("\n\t- Example: if age >= 18: print('Adult')")
            print("\n\t- Conditions evaluate True or False.")
            print()
            input("Press Enter...")


# ---------------- LOOPS MENU ----------------
def loopsfifthchoice():
    while True:
        clear()
        print("\n--------------- LOOPS ---------------")
        print("\t1 - Demo")
        print("\t2 - Explanation")
        print("\t0 - Back")
        print("\n-------------------------------------")

        try:
            choice = int(input("Enter choice: "))
        except:
            print("Numbers only.")
            continue

        if choice == 0:
            return

        elif choice == 1:
            clear()
            count = 0
            while count < 3:   # while loop
                print("Count:", count)
                count += 1
            print()
            input("Press Enter...")

        elif choice == 2:
            clear()
            print("LOOPS EXPLANATION:")
            print("\n\t- while loops repeat code while a condition is true.")
            print("\n\t- You must update the variable to avoid infinite loops.")
            print()
            input("Press Enter...")

def listssixchoice():
    while True:
        clear()
        print("\n--------------- LISTS -----------------")
        print("\t1 - Demo")
        print("\t2 - Explanation")
        print("\t0 - Back")
        print("\n-------------------------------------")

        try:
            choice = int(input("Enter choice: "))
        except:
            print("Numbers only.")
            continue

        if choice == 0:
            return

        elif choice == 1:
            clear()
            fruits = ["apple", "banana"]  # list
            fruits.append("orange")          # append
            print(fruits)
            print()
            input("Press Enter...")

        elif choice == 2:
            clear()
            print("LISTS EXPLANATION:")
            print("\t- Lists store multiple values.")
            print("\n\t- Example: fruits = ['apple', 'banana']")
            print("\n\t- Use append() to add items.")
            print("\n\t- Use indexing: fruits[0]")
            print()
            input("Press Enter...")


# ---------------- FUNCTIONS MENU ----------------
def functionsseventhchoice():
    while True:
        clear()
        print("\n--------------- FUNCTIONS ---------------")
        print("\t1 - Demo")
        print("\t2 - Explanation")
        print("\t0 - Back")
        print("\n------------------------------------------")

        try:
            choice = int(input("Enter choice: "))
        except:
            print("Numbers only.")
            continue

        if choice == 0:
            return

        elif choice == 1:
            clear()
            def greet(name):     
                return "Hello, " + name

            print(greet("User"))
            print()
            input("Press Enter...")

        elif choice == 2:
            clear()
            print("FUNCTIONS EXPLANATION:")
            print("\t- Functions organize reusable code.")
            print("\n\t- Example: def add(a,b): return a+b")
            print("\n\t- Functions can return values.")
            print()
            input("Press Enter...")


def usereighthchoice():
    while True:
        clear()
        print("\n--------------' USER PYTHON PROGRAM '--------------")
        print("\tType your Python code line by line.")
        print("\tType RUN to execute your code.")
        print("\tType 0 to go back to menu.")
        print("---------------------------------------------------")

        code_lines = []  #list

        while True:
            line = input(">   ")

            if line.upper() == "RUN":
                clear()
                print("Running your code...")

                try:                 
                    exec("\n".join(code_lines))
                except Exception as e:
                    print("Error while running code:", e)

                print()
                input("Press Enter...")
                break

            elif line.upper() == "0":
                return

            else:
                code_lines.append(line)

main_menu()


