########################################
"""
Dynamic Programming - subsequences

Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels. 
The game ends when both players have made all possible substrings. 

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points. 

For better understanding, see the image below
"""

findall_lc = lambda txt, substr: [n for n in xrange(len(txt)) if txt.find(substr, n) == n]
import re
def minion_game(string):
    # your code goes here
    vowels=set(['A','E','I','O','U'])
    s=set(string)
    l=list(s)
    svowels=s.intersection(vowels)
    vcnt=0
    ccnt=0
    while len(l) !=0:
        
        l=list(set(l))
        sorted(l,reverse=False,key=len)
        x=l.pop()
        pattern=r'(?={})'.format(x)
        #print x
        if x[0] in vowels:
            vcnt+=len(re.findall(pattern,string))
        else:
            ccnt+=len(re.findall(pattern,string))
        for i in findall_lc(string,x):
            #print i,x+string[i+]
            if i+len(x)<len(string):
                try:
                    l.append(x+string[i+len(x)])
                except:
                    print "error"
            
    if vcnt>ccnt:
        print "Kevin {}".format(vcnt)
    elif vcnt<ccnt:
        print "Stuart {}".format(ccnt)
    else:
        print "Draw"
		
if __name__ == '__main__':
    s = raw_input()
    minion_game(s)
	
	
#######################################################################
"""
max reminder to sum of max of elements from a list
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import *
n,m=map(int,raw_input().split())
x=[]
for i in range(n):
    t=raw_input().split()[1:]
    x.append(map(int,t))
Max=0
for i in product(*x):
    Max=max(sum(map(lambda a:a**2,i))%m,Max)

print Max