def avgpowerroot(x,power,epsilon=0.001):
	"""Derive power root of value with error of max 0.001"""
	low=0.0
	high=x
	steps=0
	g= (low+high)/2
	while abs(x-(g**power))>=epsilon:
		print("low is {} and high is {}".format(low,high))
		steps+=1
		if x>g**power:
			low=g
		else:
			high=g
		g = (low+high)/2


	print("no of guesses {}".format(steps))
	print("sqrt of {} is  {}".format(x,g))

def numericalsqrt(x):
	steps=0
	epsilon=0.01
	g=x/2.0
	while abs(x-(g**2))>=epsilon:
		steps+=1
		g= (g + (x/g))/2
		print("guess"+str(g))
	print("no of guesses {}".format(steps))
	print("sqrt of {} is  {}".format(x,g))

def newtonsqrt(x):
	steps=0
	epsilon=0.01
	g=x/2.0
	while abs(x-(g**2))>=epsilon:
		steps+=1
		g= g- (g**2 - x)/(2*g)
		print("guess"+str(g))
	print("no of guesses {}".format(steps))
	print("sqrt of {} is  {}".format(x,g))



avgpowerroot(12345,3)

numericalsqrt(12345)
newtonsqrt(12345)