def dict():
    di={'IN':'India','PAK':'Pakistan','US':'United States','UK':'United Kingdom'}
    for k in di:
       print(k,di[k])
    for k in sorted(di.keys()):
       print(k,di[k])
def main():
    dict()
if __name__=="__main__":main()
