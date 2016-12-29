import numpy as np

##create identity matrix
x=np.eye(3,dtype='f')
print(x)
np.savetxt('matrix.txt',x)

#loading from comma seperated file
#AAPL,28-01-2011, ,344.17,344.4,333.53,336.1,21144800
c,v=np.loadtxt('apple.csv',delimiter=',',usecols=(6,7))
print(c,v)


#statistics mean,median
print(np.mean(c))
print(np.median(c))

#matrix creation
#mat,matrix,bmat are functions used to create matrix
a=np.mat('1 2 3; 4 5 6;7 8 9')
print(a)
print(type(a))

b=np.mat(np.arange(16).reshape(4,4))
print(b)

#transpose
print(a.T)

#inverse
print(a.I)

print("Check inverse")
print(a * a.I)

# combining matrix
A=np.eye(2)
print(A)
B=2*A
C=np.bmat( 'A B ; A B')
print(C)



#zero matrix

Z=np.zeros_like(np.arange(4).reshape(2,2))
print(Z)
Z.flat=42
print(Z)


#creating functions in numpy
def numfn(a):
    Z=np.zeros_like(a)
    Z.flat=42
    return Z


ufunc=np.frompyfunc(numfn,1,1)
print(ufunc(np.arange(4)))


##add,reduce,accumulate
x=np.arange(10)
print(np.add.reduce(x))
print(np.add.accumulate(x))
