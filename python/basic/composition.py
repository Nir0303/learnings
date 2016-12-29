##other class methods from composition method rather than from inheritance
##other class
class other:
    def implicit(self):
        print("other Implicit")
    def overide(self):
        print("other Overide")
    def altered(self):
        print("other Altered")

##child class
class child:
    def __init__(self):
        self.other=other()
    def overide(self):
        print("Child Overide")
    def altered(self):
        print("Before other")
        ##altered class from other is called
        self.other.altered()
        print("After other")
    def implicit(self):
        print("Child Implicit")


c=child()
c.overide()
c.implicit()
c.altered()
