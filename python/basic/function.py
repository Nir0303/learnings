def main():
    test_function(1,2,3,34,43)

def test_function(a,b,c,*args):
    print(a,b,c,args)
    pass ###pass to define function without any def

if __name__=="__main__":main()
