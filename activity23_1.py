def greetwithname(name):
    print(f"I Greet the Esteemed Guest {name}, I hope you have a great day.")

greetwithname('Lim')

def Greetingperson(name, location, age):
    print(f"Hi, {name} from {location} , {age} yr\'s old")

def functionwithreturn(number):
    print(f"THIS FUNCTION CALCULATES THE SUMMATION FROM 1 TO {number}")
    sum = 0
    for x in range(1, number+1 , 1):
        sum += x
    return sum 
