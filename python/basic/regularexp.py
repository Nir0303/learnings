import re

def main():
  try:
    f=open("niranjan.txt")
  
    pattern=re.compile('(hell|g)o',re.IGNORECASE) ###pattern 
    h="&&&"
    for word in f:
        if re.search(pattern,word): ###searching
            print(pattern.search(word))
            print(re.sub(pattern,h,word),end="") ###replacing
            print(pattern.sub(h,word))
        
    for word in f:
        print(word)
  except IOError as e:
    print(e)  
main()
