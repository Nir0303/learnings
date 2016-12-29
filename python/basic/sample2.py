try:
    f=open('niranjan.txt')
    for i in f.readlines():
             word=i
    print("Everything seems fine")
except IOError as e:
    print("something went wrong %s" %e )
