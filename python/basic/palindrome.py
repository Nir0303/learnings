def palindrome(s):
	def tochar(s):
		s=s.lower()
		t=''
		for i in s:
			if ord(i) in range(97,122):
				t+=i
		return t


	def ispal(s):
		if len(s)<=1:
			return True
		else:
			if s[0]!=s[-1]:
				return False
			else:
				return ispal(s[1:-1])
	return ispal(tochar(s))

print palindrome('asadssa asdsad')


def palind(s)
	s=list(s)
	for 