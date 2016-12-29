##inheriting list class 
class namedlist(list):
    def __init__(self,aname,c=[]):
        list.__init__([])
        self.a=aname
        self.extend(c)

    ## Adding printout functionality to list
    def printout(self):
        print(self)

##all methods which work for list will also work for namedlist

a=namedlist('a')
a.append(5)
a.extend([1,2,3])
a.pop()
a.remove(1)
print(len(a))
print(sorted(a))
a.sort()
a.printout()
