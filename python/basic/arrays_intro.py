import numpy as np

##array is one dimensional
##arange is same as python range, arange has additional feature like element operations are done without using for loop
a=np.arange(10)
print(a)
b=a**3
print(b)
##shape is length of each dimension
print(a.shape)

## different types of arrays can be created with dtype option
""" integer i
    Unsigned integer u
    Single precision float f
    Double precision float d
    bool b
    complex D
    string S"""
print(np.arange(5,dtype='D')) 
print(np.arange(5,dtype='f'))

#array slicing
print("Print reverse order"+str(a[::-1]))
print("Print increment by 2"+str(a[::2]))
print("print 1 to 7  in a"+str(a[1:8:1]))

##ndarray is multidimensional array
x=np.ndarray([1,2,3])
print(x.shape)

##reshape is dividing array by 2 , 3 ,5
y=np.arange(6).reshape(2,3)
print(y)
print(y.shape)
print(y.reshape(3,2))
print(y)
## resize is same as reshape but it alters the array
print("resize")
y.resize(2,3)
print(y)

##transpose matrix
t=y.transpose()
print(t)
print(y.transpose()==y.T)

##setting shape
y.shape=(3,2)
print(y)


##flattening multidimension
z=y.ravel()
print(z)
print(y.flatten())


