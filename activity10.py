from getpass import getpass

username = 'Jet Lee'
password = 'jetlee123'

u = input("Username - ")
p = getpass("Password - ")

if (u == username) and (p == password) :
	print("GRANTED")
else:
	print("DENIED")