import numpy as np
a=np.mat('0 1 2;1 0 3; 4 -3 8')
print(a)

#inverse of A

b=np.linalg.inv(a)
print(b)

print(a*b)

#solving linear equations

A=np.mat("1 -2 1;0 2 -8;-4 5 9")
print(A)
B=np.array([ 0,8,-9])
#finding solution
x=np.linalg.solve(A,B)
print("Solution x {}".format(x))

#checking solution
y=np.dot(A,x)
print(y)

#finding eigenvalues and eigenvectors

A=np.mat("3 -2;1 0")
print(A)
print("Eigen Values {}".format(np.linalg.eigvals(A)))
print("Eigen numbers are {}".format(np.linalg.eig(A)))