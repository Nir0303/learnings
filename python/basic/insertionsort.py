a=[]
n=int(input())
for i in range(n):
    a.append(int(input()))
##print(a)
cnt=0
for i in range(len(a)):
   for j in range(i):
     if a[i-1-j]>a[i-j]   :
      a[i-1-j],a[i-j]=a[i-j],a[i-j-1]
      ##print(a)
      cnt+=1
print(cnt)
   
