# Paste your code into this box

balc =balance 
monthlyInterestRate = annualInterestRate/12
#minpay=balance/12.0
totalamt= balc * ((1+monthlyInterestRate)**12)
minpay = (balance)/12
while abs(balance) >100:
    balance=balc
    paid=0
    for i in range(12):
        paid+=minpay
        
        balance=(1+monthlyInterestRate)*balance
        balance-=minpay
    print balance
    if balance > 0.0:
        minpay+=1
    else:
        minpay-=1
    print(minpay,minpay*12,paid,totalamt,balc)

print("Lowest Payment: {}".format(minpay))