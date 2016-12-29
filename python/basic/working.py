def main():
### if clause
 """   a,b=10,2
    v="A is greater than B" if a>b else "B is Greater than A"
    print(v)
"""
 ###while clause
 """
 a=1
 while a<5:
    print(a)
    a+=1
"""

 ### reading lines and for loop
"""
f=open("niranjan.txt")

for word in f.readlines():
 print(word,end=',')
"""
### Enumerators
"""
f=open("niranjan.txt")
for i,word in enumerate(f.readlines()):
               print(i,word)
"""

### break continue and else control loops
"""
i="Niranjan"
for a in i:
    if a=="i": break
    print(a,end='')
    if a=="i": continue
    print(a,end='')    
main()
"""
print( 5//3) ###integer division
print(5/3) ###Normal division
print(5%3) ###Reminder
print(divmod(5,2)) ###Divident and reminder

##binary convertion
def binary(a):
	print("{:08b}".format(a))

a,b=0x55,0x11
binary(a)
binary(b)
binary(a&b)
binary(a|b)

x=[5]
y=[5]
print(x is y) ###compares ids
x=5
y=5
print(x is y) ###compares ids

