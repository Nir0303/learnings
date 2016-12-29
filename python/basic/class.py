class animal:
    def walk(self): print("Hey I'm walking")
    def talk(self):print("Hey i'm blabering")

class duck(animal):
    def __init__(self,**kargs):
        self.variable=kargs
        print("constructor")
    def walk(self):
        print("Walk like a duck")
    def eat(self):
        print("Eat like a duck")
    def change_variable(self,k,value):
        self.variable[k]=value
    def get_variable(self,k):
        return self.variable[k]


    

def main():
    donald=duck(color="blue",hieght=42)
    donald.walk()
    donald.eat()
    print(donald.get_variable("color"))
    donald.change_variable("color","white")
    print(donald.get_variable("hieght"))
    print(donald.get_variable("color"))
    donald.talk()

if __name__=="__main__": main()
