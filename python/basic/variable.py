def samplefun():
    a=10
    print(a,type(a),id(a))
    a=10.0
    print(a,type(a),id(a))
    a=float(10)
    print(a,type(a),id(a))
    a=10/3
    print(a,type(a),id(a))
    a=10//3
    print(a,type(a),id(a))
    a=10%3
    print(a,type(a),id(a))
    a=10
    print(a,type(a),id(a))

def main():
    samplefun()

if __name__=="__main__": main()
