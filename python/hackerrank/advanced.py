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


#######################################################################
"""
groupby no of elements
Sample Input

1222311
Sample Output

(1, 1) (3, 2) (1, 3) (2, 1)
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import print_function
from itertools import groupby

groups=[]
uniquekeys=[]
for k, g in groupby(raw_input()):
    groups.append((len(list(g)),int(k)))
for i in groups:
    print(i,end=" ")
	
###########################################################################

"""
In this challenge, you will be given  integers,  and . There are  words, which might repeat, in word group . 
There are  words belonging to word group . For each  words, check whether the word has appeared in group  or not.
 Print the indices of each occurrence of  in group . If it does not appear, print .

Constraints 

Sample Input

5 2
a
a
b
a
b
a
b
Sample Output

1 2 4
3 5

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
m,n=map(int,raw_input().split())
d=defaultdict(list)
for i in range(1,m+1):
    d[raw_input()].append(i)
for i in range(n):
    print ' '.join(map(str,d.get(raw_input(),[-1])))
###################################################################################
"""
Dr. John Wesley has a spreadsheet containing a list of student's , ,  and .

Your task is to help Dr. Wesley calculate the average marks of the students.


Note: 
1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet. 
2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)

Input Format

The first line contains an integer , the total number of students. 
The second line contains the names of the columns in any order. 
The next  lines contains the , ,  and , under their respective column names.

Constraints


Output Format

Print the average marks of the list corrected to 2 decimal places.

Sample Input

TESTCASE 01

5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   
TESTCASE 02

5
MARKS      CLASS      NAME       ID        
92         2          Calum      1         
82         5          Scott      2         
94         2          Jason      3         
55         8          Glenn      4         
82         2          Fergus     5
Sample Output

TESTCASE 01

78.00
TESTCASE 02

81.00
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
import re
n=input()
x=raw_input()
columns=",".join(re.split(r'\s*',x))
marks=namedtuple('marks',columns.rstrip(','))
d=[]
#print marks.index,marks._fields
for i in range(n):
    x=raw_input()
    columns=re.split(r'\s*',x)
    
    m=marks(columns[0],columns[1],columns[2],columns[3])
    d.append(m)
m=0
for i in d:
    m+=float(i.MARKS)
print m/n

################################################################################
"""
combinations with replacements

Sample Input

HACK 2
Sample Output

AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
s,n=raw_input().split()
A=[]
s=sorted(s)
for i in list(combinations_with_replacement(s,int(n))):
    print ''.join(sorted(i))
	
###################################################################################
"""
collection counters 

Task

 is a shoe shop owner. His shop has  number of shoes. 
He has a list containing the size of each shoe he has in his shop. 
There are  number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.

Your task is to compute how much money  earned.

Sample Input

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
Sample Output

200

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
from collections import Counter 
shoes=Counter(map(int,raw_input().split()))
prices=0
for i in range(input()):
    x=map(int,raw_input().split())
    if shoes.get(x[0],None)!=0 and shoes.get(x[0],None) is not None  :
        shoes[x[0]]-=1
        prices+=x[1]
print prices



######################################################################################
"""
display cart list in order
Sample Input

9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
Sample Output

BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
Explanation

BANANA FRIES: Quantity bought: , Price:  
Net Price:  
POTATO CHIPS: Quantity bought: , Price: 
Net Price:  
APPLE JUICE: Quantity bought: , Price:  
Net Price:  
CANDY: Quantity bought: , Price:  
Net Price: 
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
import re
items=OrderedDict()
cost={}
for i in range(input()):
    t=raw_input()
    x=t.split()
    t= re.split(r'\s\d+',t)
    v=t[0]
    if items.get(v,None) is  None:
        items[v]=i
        cost[v]=int(x[-1])
    else:
        cost[v]+=int(x[-1])

for i in items:
    print i,cost[i]
	
########################################################################
"""
Input Format

The first line contains the integer,n . 
The next n lines each contain a word.

Output Format

Output 2 lines. 
On the first line, output the number of distinct words from the input. 
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

Sample Input

4
bcdef
abcdefg
bcde
bcdef
Sample Output

3
2 1 1

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import print_function
from collections import Counter,OrderedDict 
t=[]
d=OrderedDict()
for i in range(input()):
    x=raw_input()
    if d.get(x,None) is not None:
        d[x]+=1
    else:
        d[x]=1
print(len(set(d)))
for i in d:
    print(d[i],end=" ")
	
############################################################
"""
left most side is greater than right most side print true , else false
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(input()):
    x=input()
    t=map(int,raw_input().split())
    if all(t[i]>=t[len(t)-1-i] for i in range(len(t)/2) ) :
        print "Yes"
    else:
        print "No"
#############################################################
"""
most common elements
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
counter = Counter(list(raw_input()))
for i in counter.most_common(3):
    print i[0],i[1]
