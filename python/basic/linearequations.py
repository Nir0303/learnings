import numpy as np
from matplotlib.pyplot import plot,show

##creating linespaces between 2 points
t=np.linspace(-np.pi,np.pi,1000)
print(t)
a=2
b=1
x=np.sin( a*t + np.pi/2)
y=np.sin(b*t)

##ploting with matplotlib
plot(x,y)
show()