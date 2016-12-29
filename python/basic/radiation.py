def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)


def radiationExposure(start, stop, step):
	sumq=0
	start=float(start)
	stop=float(stop)
	while start<stop:
		sumq+=f(start)*step
		start+=step
	return sumq