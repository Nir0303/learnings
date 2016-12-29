#declaring class
class test:
    #initializing class variables 
    def __init__(self,a='a'):
        self.a=a
    #declaring method in test class
    def how_big(self):
        print(len(self.a))
a=test()
a.how_big()
    
