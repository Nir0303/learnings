import string
def isWordGuessed(secretWord, lettersGuessed):
	secretWord=list(secretWord)
	lettersGuessed=set(lettersGuessed)
	cnt=0
	for i in lettersGuessed:
		cnt+=secretWord.count(i)
	return len(secretWord)==cnt


def getGuessedWord(secretWord, lettersGuessed):
	secretWord=list(secretWord)
	lettersGuessed=list(set(lettersGuessed))
	x='_'*len(secretWord)
	x=list(x)
	for i in range(len(lettersGuessed)):
		for j in range(len(secretWord)):
			if secretWord[j]==lettersGuessed[i]:
				x[j]=secretWord[j]
	return ''.join(x)


def getAvailableLetters(lettersGuessed):
	lowercase=string.ascii_lowercase
	lowercase=set(lowercase)-set(lettersGuessed)
	return ''.join(sorted(list(lowercase)))


def flatten(aList):
    if aList==[]:
    	return aList
    if isinstance(aList[0],list):
    	return flatten(aList[0]) + flatten(aList[1:])
    else:
        return aList[:1] + flatten(aList[1:])

def f(s):
	return 'a' in s 


def dict_interdiff(d1, d2):
	k1=set(d1.keys())
	k2=set(d2.keys())
	inter=k1.intersection(k2)
	diff=k1.symmetric_difference(k2)
	x={}
	for i in list(inter):
		x[i]= f(d1[i],d2[i])
	y={}
	for j in list(diff):
		if d1.get(j,None) is not None:
			y[j]=d1[j]
		else:
			y[j]=d2[j]
	return (x,y)

# Paste your function here
def satisfiesF(L):
    x=list(L)
    for i in L:
        if not f(i):
            x.remove(i)
    return len(L)


def is_leap(year):
	year=int(year)
	leap=False
	if year%400==0:
		leap=True
	elif year%100==0:
		leap=False
	elif year%4==0:
		leap=True
	return leap

def divide(x,y):
	try:
		print(x/y)
	except ZeroDivisionError,e:
		print(e)
	else:
		print("Execution is successful")
	finally:
		print("End")

def genSubsets(L):
 res = []
 if len(L) == 0:
 	return [[]]
 smaller = genSubsets(L[:-1])
 extra = L[-1:]
 new = []
 for small in smaller:
 	new.append(small+extra)
 return smaller+new


def search(L,x):
 	def bsearch(L,x,low,high):
 		if low==high:
 			return L[low]==x,low
 		mid=(low+high)/2
 		if L[mid]>x:
 			return bsearch(L,x,low,mid)
 		elif L[mid]==x:
 			return True,mid
 		else:
 			return bsearch(L,x,mid+1,high)
 	if len(L)==0:
 		return False
 	else:
 		return bsearch(L,x,0,len(L)-1)

def selectionsort(L):
	for i in range(len(L)):
		minIndex=i
		minValue=L[i]
		j=i+1	
		while j <=len(L)-1:
			if minValue > L[j]:
				minValue,L[j]=L[j],minValue
			j+=1

			L[i]=minValue
			return L

def mergeSort(L):
	if len(L) < 2:
		return L[:]
	else:
		mid=(len(L))/2
		left=mergeSort(L[:mid])
		right=mergeSort(L[mid:])
		return merge(left,right)

def merge(left,right):
	j=0
	i=0
	result=[]
	while j<len(left) and i<len(right):
		if left[j] < right[j]:
		 	result.append(left[j])
		 	j+=1
		else:
		 	result.append(right[i])
		 	i+=1
	if j<len(left):
		result.extend(left[j:])
	if i<len(right):
		result.extebd(right[i:])
	return result