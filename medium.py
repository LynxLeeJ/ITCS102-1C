price = eval(input("Item Price --> "))
quan = eval(input("Quantity --> "))

total = price * quan

if total >= 100:
	discount = total * 0.10
	new_total = total - discount
	print("The discount has been applied", discount , "Your new total is", new_total)
else:
	print("Discount is not applicable, ORIGINAL PRICE" , total)