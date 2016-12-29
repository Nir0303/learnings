class fib():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def series(self):
        while(True):
            yield(self.b)
            self.a,self.b=self.b,self.a+self.b
f =fib(0,1)
for i in f.series():
    if i>100: break
    print ("%d" %i)
