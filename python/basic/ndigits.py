def ndigits(x):
    ##take absolute value of number
    x=abs(x)
    if x==0:
        ##return zero is number is 0 to stop recursive loop
        return 0
    else:
        ##recursive call
        return 1 + ndigits(x/10)