import sys 
import os   

def main_menu():
    """
    Displays the main menu with options for Python fundamentals topics.
    Handles user input and navigation to submenus.
    """
    while True:
        print("\n" + "="*50)
        print("Fundamentals of Computer Programming")
        print("Interactive Menu Program \n - Main Menu")
        print("="*50)
        print("1. Print Statements")
        print("2. Variables")
        print("3. Operators")
        print("4. Conditionals")
        print("5. Loops")
        print("6. Lists")
        print("7. Functions")
        print("0. Exit")
        print("="*50)
        
        try:                                    #try/except in while loop makes your code dont crash when entering the wrong input
            choice = int(input("Enter your choice (0-7): "))  
            if choice == 0:
                print("Exiting the program. Goodbye!")
                sys.exit()
            elif choice == 1:
                print_statements_menu()
            elif choice == 2:
                variables_menu()
            elif choice == 3:
                operators_menu()
            elif choice == 4:
                conditionals_menu()
            elif choice == 5:
                loops_menu()
            elif choice == 6:
                lists_menu()
            elif choice == 7:
                functions_menu()
            else:
                print("Invalid choice. Please select a number between 0 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def print_statements_menu():
    """
    Submenu for Print Statements: Includes demo and concise explanation.
    """
    os.system('cls')
    while True:
        print("\n" + "-"*40)
        print("Print Statements")
        print("-"*40)
        print("1. View Example and Run Demo")
        print("2. Explanation")
        print("0. Back to Main Menu")
        
        try:
            choice = int(input("Enter your choice (0-2): "))
            if choice == 0:
                break
            elif choice == 1:
                print("\nExample: Basic print statement")
                print("Code: print('Hello, World!')")
                print("Output:")
                print("Hello, World!")
            elif choice == 2:
                print("\nExplanation:")
                print("- Print statements display text or values on the screen using the print() function.")
                print("- Usage: print('message') or print(variable). Use commas for multiple items.")
                print("- Example: print('Sum:', 5 + 3) shows 'Sum: 8'.")
                print("- Tip: Use f-strings like print(f'Hello {name}') for formatting.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input.")

def variables_menu():
    """
    Submenu for Variables: Includes demo and concise explanation.
    """
    os.system('cls')  
    while True:
        print("\n" + "-"*40)
        print("Variables")
        print("-"*40)
        print("1. View Example and Run Demo")
        print("2. Explanation")
        print("0. Back to Main Menu")
        
        try:
            choice = int(input("Enter your choice (0-2): "))
            if choice == 0:
                break
            elif choice == 1:
                print("\nExample: Assigning and printing variables")
                x = 10
                name = "Python"
                print(f"Code: x = 10; name = 'Python'; print(x, name)")
                print("Output:")
                print(x, name)
            elif choice == 2:
                print("\nExplanation:")
                print("- Variables store data values, like numbers or text, for reuse in the program.")
                print("- Usage: Assign with =, e.g., age = 25. Names start with a letter or _.")
                print("- Types: int (numbers), str (text), float (decimals), bool (True/False).")
                print("- Example: score = 100; print(score) shows 100.")
                print("- Tip: Use clear names like user_name to make code easy to read.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input.")

def operators_menu():
    """
    Submenu for Operators: Includes demo and concise explanation.
    """
    os.system('cls') 
    while True:
        print("\n" + "-"*40)
        print("Operators")
        print("-"*40)
        print("1. View Example and Run Demo")
        print("2. Explanation")
        print("0. Back to Main Menu")
        
        try:
            choice = int(input("Enter your choice (0-2): "))
            if choice == 0:
                break
            elif choice == 1:
                print("\nExample: Arithmetic operators")
                a = 5
                b = 3
                print(f"Code: a = 5; b = 3; print(a + b, a * b)")
                print("Output:")
                print(a + b, a * b)
            elif choice == 2:
                print("\nExplanation:")
                print("- Operators perform actions like math or comparisons on values.")
                print("- Types: Arithmetic (+, -, *, /), Comparison (==, >, <), Logical (and, or).")
                print("- Usage: result = a + b or if x > 5.")
                print("- Example: 5 > 3 is True; 'hi' + 'there' makes 'hithere'.")
                print("- Tip: Use parentheses for order, like (a + b) * c.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input.")

def conditionals_menu():
    """
    Submenu for Conditionals: Includes demo and concise explanation.
    """
    os.system('cls') 
    while True:
        print("\n" + "-"*40)
        print("Conditionals")
        print("-"*40)
        print("1. View Example and Run Demo")
        print("2. Explanation")
        print("0. Back to Main Menu")
        
        try:
            choice = int(input("Enter your choice (0-2): "))
            if choice == 0:
                break
            elif choice == 1:
                print("\nExample: If-else statement")
                num = 10
                if num > 5:
                    result = "Greater than 5"
                else:
                    result = "Not greater than 5"
                print(f"Code: num = 10; if num > 5: print('Greater than 5') else: print('Not')")
                print("Output:")
                print(result)
            elif choice == 2:
                print("\nExplanation:")
                print("- Conditionals run different code based on true/false checks.")
                print("- Usage: if condition: do this elif another: do that else: default.")
                print("- Example: if age >= 18: print('Adult') else: print('Minor').")
                print("- Tip: Indent code under if/else and use == for comparisons.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input.")

def loops_menu():
    """
    Submenu for Loops: Includes demo and concise explanation.
    """
    os.system('cls')  
    while True:
        print("\n" + "-"*40)
        print("Loops")
        print("-"*40)
        print("1. View Example and Run Demo")
        print("2. Explanation")
        print("0. Back to Main Menu")
        
        try:
            choice = int(input("Enter your choice (0-2): "))
            if choice == 0:
                break
            elif choice == 1:
                print("\nExample: While loop")
                print("Code: count = 0; while count < 3: print(count); count += 1")
                print("Output:")
                count = 0
                while count < 3:
                    print(count)
                    count += 1
            elif choice == 2:
                print("\nExplanation:")
                print("- Loops repeat code multiple times to automate tasks.")
                print("- Types: For (over lists or ranges), While (while condition is true).")
                print("- Usage: for item in list: or while x < 10:.")
                print("- Example: for i in range(5): print(i) prints 0 to 4.")
                print("- Tip: Use break to stop early and avoid infinite loops.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input.")

def lists_menu():
    """
    Submenu for Lists: Includes demo and concise explanation.
    """
    os.system('cls')  
    while True:
        print("\n" + "-"*40)
        print("Lists")
        print("-"*40)
        print("1. View Example and Run Demo")
        print("2. Explanation")
        print("0. Back to Main Menu")
        
        try:
            choice = int(input("Enter your choice (0-2): "))
            if choice == 0:
                break
            elif choice == 1:
                print("\nExample: List operations")
                my_list = [1, 2, 3]
                my_list.append(4)
                print(f"Code: my_list = [1,2,3]; my_list.append(4); print(my_list)")
                print("Output:")
                print(my_list)
            elif choice == 2:
                print("\nExplanation:")
                print("- Lists store multiple items in order, like a collection.")
                print("- Usage: Create with [], access with index (list[0]), add with append().")
                print("- Example: fruits = ['apple', 'banana']; fruits.append('orange').")
                print("- Tip: Use len() for size and slicing like [1:3] for parts.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input.")

def functions_menu():
    """
    Submenu for Functions: Includes demo and concise explanation.
    """
    os.system('cls')  
    while True:
        print("\n" + "-"*40)
        print("Functions")
        print("-"*40)
        print("1. View Example and Run Demo")
        print("2. Explanation")
        print("0. Back to Main Menu")
        
        try:
            choice = int(input("Enter your choice (0-2): "))
            if choice == 0:
                break
            elif choice == 1:
                print("\nExample: Defining and calling a function")
                def greet(name):
                    return f"Hello, {name}!"
                print("Code: def greet(name): return f'Hello, {name}!'; print(greet('User'))")
                print("Output:")
                print(greet("User"))
            elif choice == 2:
                print("\nExplanation:")
                print("- Functions are blocks of reusable code that do specific jobs.")
                print("- Usage: def name(params): code; call with name(args).")
                print("- Example: def add(a, b): return a + b; result = add(5, 3).")
                print("- Tip: Use return to send back values and keep code organized.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input.")


if __name__ == "__main__":
    main_menu()
