def recmul(a,b):
	if b==1:
		return a
	else:
		return a + recmul(a,b-1)