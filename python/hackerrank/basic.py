"""

Output Format

Print the contents of  to stdout.

Sample Input

How many chickens does it take to cross the road?

"""

def read():
    s = raw_input()
    return s

####################################################
"""
Read two integers from STDIN and print three lines where:
The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
"""
a=int(raw_input())
b=int(raw_input())
print a+b
print a-b
print a*b



################################################
"""
Read two integers and print two lines. 
The first line should contain integer division, 
// . The second line should contain float division,  / .
"""

from __future__ import division
if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print a//b
    print a/b
	
	
##################################################
"""
Read an integer . For all non-negative integers , print .
"""

if __name__ == '__main__':
    n = int(raw_input())
    for i in range(n):
        print i**2
		
#################################################

"""
In the Gregorian calendar three criteria must be taken into account to identify leap years:
The year can be evenly divided by 4;
If the year can be evenly divided by 100, it is NOT a leap year, unless;
The year is also evenly divisible by 400. Then it is a leap year.
"""

def is_leap(year):
    leap = False
    if year%400==0 or (year%4==0 and year%100!=0):
        return True
    return leap
year = int(raw_input())
print is_leap(year)


#################################################

"""
Read an integer .
Without using any string methods, try to print the following:
o/p: 123..N
"""

from __future__ import print_function
if __name__ == '__main__':
    n = int(raw_input())
    print("".join(list(map(str,range(1,n+1)))))

###################################################

"""
Sample Input

12
insert 0 5
insert 1 10
insert 0 6
print 
remove 6
append 9
append 1
sort 
print
pop
reverse
print
Sample Output

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""	
	
if __name__ == '__main__':
    N = int(raw_input())
    A=[]
    for i in range(N):
        x=str(raw_input())
        y= x.split()
        
        if x.startswith('insert'):
            A.insert(int(y[1]),int(y[2]))
        elif x.startswith('remove'):
            A.remove(int(y[1]))
        elif x.startswith('append'):
            A.append(int(y[1]))
        elif x.startswith('pop'):
            A.pop()
        elif x.startswith('sort'):
            A.sort()
        elif x.startswith('reverse'):
            A.reverse() 
        else:
            print A
####################################

"""
i <= x j<=y k<=z i+j+k !=N
Sample Input

1
1
1
2
Sample Output

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]] 

"""
			
			
if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    print  [ [i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]
#########################################
""""

second largest element in a list
"""

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr=list(set(arr))
    maxint=max(arr)
    arr.remove(maxint)
    print max(arr)
######################################

"""
Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.
"""

from collections import defaultdict
d=defaultdict(list)
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    d[score].append(name)
secondmax=sorted(d.keys())[1]

for i in sorted(d[secondmax]):
    print i

#####################################
"""
You have a record of  students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. 
The marks can be floating values. The user enters some integer  followed by the names and marks for  students. You are required to save the record in a dictionary data type.
 The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.
"""

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    ##format 2 float
    print "{0:.2f}".format(float(sum(student_marks.get(query_name,[])))/len(student_marks.get(query_name,[])))

	
###################################
"""
Swap Case upper to lower and vice versa
"""

def swap_case(s):
    t=''
    for i in s:
        x=ord(i)
        if x<=90 and x>=65:
            t+=chr(x+32)
        elif x>=97 and x<=122:
            t+=chr(x-32)
        else:
            t+=i
            
    return t
if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result

#######################################

"""
string split and join
i/p: this is a string  
o/p: this-is-a-string
"""

def split_and_join(line):
    line=line.split()
    return '-'.join(line) 	
	
if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result
	
	
#######################################

"""
No of substrings
"""


def count_substring(string, sub_string):
    cnt=0
    for i in range(0,len(string)):
        if string[i:i+len(sub_string)]==sub_string:
            cnt+=1
    return cnt 
	
	
if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count

############################################
"""
string replacement method 
(Strings are immutable)
"""

def mutate_string(string, position, character):
    ##list method
    s=list(string)
    s[position]=character
    s= ''.join(s)
    ##concentate method
    string = string[:position]+character+string[position+1:]
    return string

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new
	
################################################
"""
In the first line, print True if  has any alphanumeric characters. Otherwise, print False. 
In the second line, print True if  has any alphabetical characters. Otherwise, print False. 
In the third line, print True if  has any digits. Otherwise, print False. 
In the fourth line, print True if  has any lowercase characters. Otherwise, print False. 
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
Sample Input

qA2

Sample Output

True
True
True
True
True
"""

if __name__ == '__main__':
    s = raw_input()
    print any(i.isalnum() for i in s)
    print any(i.isalpha() for i in s)
    print any(i.isdigit() for i in s)
    print any(i.islower() for i in s)
    print any(i.isupper() for i in s)
	
	
	
###########################################
"""
Sample Input

5
Sample Output

    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH        	     
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H 

"""


#Replace all ______ with rjust, ljust or center. 

thickness = int(raw_input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print (c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1)

#Top Pillars
for i in range(thickness+1):
    print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)

#Middle Belt
for i in range((thickness+1)/2):
    print (c*thickness*5).center(thickness*6)    

#Bottom Pillars
for i in range(thickness+1):
    print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)    

#Bottom Cone
for i in range(thickness):
    print ((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6)    

##########################################

"""
textwrap.wrap --> to do text wrapping
text.fill --> to print string in fill format
"""

def wrap(string, max_width):
    return '\n'.join(textwrap.wrap(string,max_width))

if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print result
	
	
############################################
"""
Sets distinct 
"""

from __future__ import division

def average(array):
    # your code goes here  
    x=set(array)
    return sum(x)/len(x)
	
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result
	
###############################################
"""
Sets Symmetric difference
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
N=input()
A=set(map(int,raw_input().split()))
M=input()
B=set(map(int,raw_input().split()))
for i in sorted(list(A.symmetric_difference(B))):
    print i
	
	
###############################################
"""
disjoint sets example
There is an array of  integers. There are also  disjoint sets,  and , each containing  integers. 
You like all the integers in set  and dislike all the integers in set . Your initial happiness is .
 For each  integer in the array, if , you add  to your happiness.
 If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
m,n=raw_input().split()
A=list(map(int,raw_input().split()))
B=set(map(int,raw_input().split()))
C=set(map(int,raw_input().split()))
notC=B.difference(C)
notB=C.difference(B)
print len(filter(lambda i: i in notC,A ))-len(filter(lambda i: i in notB,A ))

####################################################
"""
distinct elements
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
print len(list({ raw_input() for i  in range(n) }))


######################################################
#union

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
A=set(map(int,raw_input().split()))
m=input()
B=set(map(int,raw_input().split()))
print len(A.union(B))
print len(A.difference(B))
print len(A.symmetric_difference(B))
print len(A.intersection(B))


###########################################################
"""
mutable insertation update,intersection_update,symmetric_difference_update,difference_update
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
A = set(map(int, raw_input().split())) 
for j in range(input()):
    i=raw_input()
    k=set(map(int, raw_input().split())) 
    x=i.split()
    if i.startswith('intersection_update'):
        A.intersection_update(k)
    elif i.startswith('update '):
        A.update(k)
    elif i.startswith('symmetric_difference_update'):
        A.symmetric_difference_update(k)

    elif i.startswith('difference_update'):
        A.difference_update(k)

print sum(map(int,A))


############################################################
"""
Strict super set
Sample Input

1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12
Sample Output

False
Explanation

Set  is the strict superset of the set but not of the set because  is not in set .
Hence, the output is False.

"""

A=set(map(int,raw_input().split()))
n=input()
print all(len(set(map(int,raw_input().split())).difference(A))==0 for i in range(n) )


#############################################################
"""
Pyramid

1
121
12321
1234321
"""

for i in range(1,input()+1):
	print ((10**i-1)//9)**2


	
#########################################################################
"""
divisor,dividend,mod
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
x=input()
print n//x
print n%x
print divmod(n,x)


#######################################################################
"""
power and power mod
"""

n=input()
p=input()
m=input()
print pow(n,p)
print pow(n,p,m)