loan = eval(input("Enter Loan Amount ---> "))
loan_period = eval(input("Enter Loan Amount Period in Years ---> "))
loan_period *= 12
balance = loan
principal = loan / loan_period
print("PAYMENT SCHEDULE")
print("MONTH\t|\t MONTHLY PAYMENT\t|\tINTEREST\t|\tPRINCIPAL\t|\tREMAINING BALNCE\t|")
print("________________________________________________________________________________________________________________")
for i in range(1, loan_period + 1, 1):
    balance -= principal 
    interest = balance * 0.003
    monthly = principal + interest
    print(f"{i}\t|\t{round(principal,2)}\t\t\t|\t{round(balance, 2)}\t\t|\t{round(interest,2)}\t\t|\t{round(monthly, 2)}")