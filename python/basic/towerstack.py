def printmov(fr,to):
	print "move {} from {}".format(fr,to)

def towerstack(n,fr,to,s):
	if n==1:
		printmov(fr,to)
	else:
		towerstack(n-1,fr,s,to)
		towerstack(1,fr,to,s)
		towerstack(n-1,s,to,fr)