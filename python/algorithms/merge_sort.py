

def merge_sort(A):
	if len(A)<2 : return A
	m=len(A)/2
	return merge(merge_sort(A[:m]),merge_sort(A[m:]))

def merge(l,r):
	result=[]
	i=j=0
	while i <len(l) and j < len(r):
		if l[i] < r[j]:
			result.append(l[i])
			i+=1
		else:
			result.append(r[j])
			j+=1
	result.extend(l[i:])
	result.extend(r[j:])
	return result


t=open("myintegers.txt")
y=[]
for i in t.readlines():
	x=i.split('\n')
	y.append(int(x[0]))

print merge_sort(y)