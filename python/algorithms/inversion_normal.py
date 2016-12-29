t=open("myintegers.txt")
y=[]
for i in t.readlines():
	x=i.split('\n')
	y.append(int(x[0]))
#print y
cnt=0
for i in range(len(y)):
	for j in range(i+1,len(y)):
		if y[i] > y[j]:
			cnt+=1
print cnt