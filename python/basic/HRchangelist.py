

def changelist(args,a):
    ##print(args)
    if args[0] in "insert":
        a.insert(int(args[1]),int(args[2]))
        return a
    elif args[0] in "remove":
        a.remove(int(args[1]))
        return a
    elif args[0] in "print":
         print(a)
         return a
    elif args[0] in "remove":
         a.remove(int(args[1]))
         return a
    elif args[0] in "append":
          a.append(int(args[1]))
          return a
    elif args[0] in "sort":
          a.sort()
          return a
    elif args[0] in "reverse":
          a.reverse()
          return a
    elif args[0] in "count":
          print(a.count())
          return a
    elif args[0] in "pop":
          a.pop()
          return a   
                  
    print(a)

def main():
    n=int(input())
    a=[]
    for i in range(n):
       w=input()  
       x=changelist(w.split(),a)


main()
