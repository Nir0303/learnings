class egg:
    def __init__ (self,type="egg"):
        self.type=type
    def whatkind(self):
        return self.type
def main():
    scarmbledegg=egg("scarmbled")
    plainegg=egg()
    print(scarmbledegg.whatkind())
    print(plainegg.whatkind())

if __name__=="__main__": main()
