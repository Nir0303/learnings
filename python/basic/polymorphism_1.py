#dog class
class dog:
    def __init__(self,name):
        self.name=name
    def sound(self):
        print("Boo Boo")
#cat class
class cat:
    def __init__(self,name):
        self.name=name
    def sound(self):
        print("Meow Meow")



def makesound(atype):
    atype.sound()


stew=dog('stew')
tom=cat('tom')

#same function is called but different outputs
makesound(stew)
makesound(tom)
