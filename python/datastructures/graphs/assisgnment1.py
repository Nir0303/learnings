import random
import pprint
import numpy as np
n=input()
arr=[[0 for i in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if i!=j:
            arr[i][j]=arr[j][i]=random.randint(1,20)
pprint.pprint(arr)