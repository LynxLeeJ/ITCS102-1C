factorial = 1
number = eval(input("Enter a number --> "))
for loop in range(number,0,-1):
	factorial *= loop

print("The factorial of", number, " is", factorial)