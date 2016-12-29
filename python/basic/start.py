d = {}
x=""
a=int(input())
for i in range(a):
    b = input()
    c = b.split()
    ##print (b,c)
    avg=float(c[1])+float(c[2])+float(c[3])
    ##print( c[0],avg)
    d["Name"]=c[0]
    d["avg"]=avg
    x+=c[0]+" "
    x+=str(avg)+" "
    print(x)

name=x.split()
print(name)
y=input()
for i in name:
    if i in y:
        print(name[y.index(i)+1])
    
    
