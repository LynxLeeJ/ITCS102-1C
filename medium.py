#Multiplication Table

col = eval(input("Enter number of columns ---> "))

for i in range(1,11,1):
    for k in range(1,col+1,1):
        print(f"{i}x{k}={i*k}",end="\t\t")
    print()
