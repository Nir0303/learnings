def primenum(n):
    count=0
    if n == 1:
        print("1 is special case")
    else:    
        for x in range(2,n):
           if n%x==0 and count==0:
             print("%d %d*%d is not a prime number" %(n,x,n/x))
             count=count+1
        if count==0:
               print("%d is a prime number"%n)
                 

             
def iterator(n = 1):
    for i in range(1,100):
        yield i


for n in iterator():
    primenum(n)
