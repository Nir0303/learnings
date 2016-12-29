import sys

class animal:
    def __init__(self,name):
        self.name=name
    def printout(self):
        print(self.name)
        print("{} says {}".format(self.name,self.says))
#dog inherited from animal class
class dog(animal):
    def __init__(self,name):
        self.name=name
        self.says="Boo Boo"

#cat inherited from animal class
class cat(animal):
    def __init__(self,name):
        self.name=name
        self.says="Meow Meow"


class human:
    def __init__(self,name):
        self.name=name
        self.pet=None
    def printout(self):
        print("{} has pet {}".format(self.name,self.pet))

#student inherited from human class
class student(human):
    def __init__(self,name):
        self.name=name

#teacher inherited from human class
class teacher(human):
    def __init__(self,name):
        self.name=name



tom=dog('Tommy')
tom.printout()
Nir=student('Niranjan')
Nir.pet=tom.name
Nir.printout()
