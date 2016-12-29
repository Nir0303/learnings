import numpy as np
x=np.arange(9).reshape(3,3)
print(x)
y=x**2
print(y)

##stacking elements
##hstack horizontal stacking
print("Horizontal stacking")
print(np.hstack((x,y)))
print("Horizontal stacking with concatenate")
print(np.concatenate((x,y),axis=1))

##vstack vertical stacking
print("Vertical stacking")
print(np.vstack((x,y)))
print("vertical stacking with concatenate")
print(np.concatenate((x,y),axis=0))


##dstack depth stacking, stacking element one by one
print("Depth stacking")
print(np.dstack((x,y)))


#Splitting arrays
print("horizontal split")
print(np.hsplit(x,3))
print("Horizontal split with split")
print(np.split(x,3,axis=1))


print("Vertical Split")
print(np.vsplit(x,3))
print("vertical split with split")
print(np.split(x,3,axis=0))

##dsplit works on 3*3 martix
print("Depth split")
z=np.arange(27).reshape(3,3,3)
print(np.dsplit(z,3))

##ndim gives no of dimensions
print(z.ndim)
##size gives size of the array
print(z.size)

##converting array to list
print(type(z.tolist()))
