temp = eval(input("Enter Temperature outside --> "))

if temp <= 0:
	print("The temperature is FREEZING")
elif temp >= 1 and temp <= 20:
	print("The temperature is COLD")
elif temp >= 21 and temp <= 30:
	print("The temperature is MODERATELY COLD")
elif temp >= 31 and temp <= 37:
	print("The temperature is LUKEWARM")
elif temp >= 38 and temp <= 45:
	print("The temperature is HOT")
elif temp >= 46 and temp <= 50:
	print("The temperature is BOILING HOT")
elif temp >= 51:
	print("The temperature is DANGEROUS")	 
else:
	print("Invalid Temperature")
