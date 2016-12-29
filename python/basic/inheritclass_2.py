#parent class
class parent:
    def implicit(self):
        print("Parent Implicit")
    def overide(self):
        print("Parent Overide")
    def altered(self):
        print("Parent Altered")

#child class inheriting parent class
class child(parent):
    #parent method is overided with child method
    def overide(self):
        print("Child Overide")
        
    def altered(self):
        print("Before Parent")
        #altered method from parent class is called
        super(child,self).altered()
        print("After parent")

c=child()

p=parent()

print("-----")

c.implicit()
print("-----")
p.implicit()

print("-----")

c.overide()
print("-----")
p.overide()

print("-----")

c.altered()
print("-----")
p.altered()
