a=[]
n=int(input())
q=input()
a=q.split()
##print(a)
cnt=0
for i in range(len(a)):
   for j in range(i):
     if int(a[i-1-j])>int(a[i-j])   :
      a[i-1-j],a[i-j]=a[i-j],a[i-j-1]
      print(a)
      cnt+=1
print(cnt)
