name = input("Please Enter Your Name >>>")
fare = eval(input("Fare fee >>> "))
student = input("Are you a Student? (yes / no) ")

if student.lower() == "yes":
	discount = fare * 0.2
	new_fare = fare - discount
	print("HI", name, "Your discount is" , discount, "Your new fare is" , new_fare)
else:
	print("HI", name, "You're only eligible for regular price")

