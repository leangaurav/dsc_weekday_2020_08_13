import sys

# Python3 program to count total anagram 
# substring of a string 
def anangram_chk(st1,st2): 
   
	l1 = len(st1)
	l2 = len(st2)

	if l1 != l2:
		return 0

	else:
		print(st1,st2)
		st1 = sorted(st1) 
		st2 = sorted(st2) 

		for i in range(0, l1):  
			if st1[i] != st2[i]:  
				return 0
		#print(repr(st1),repr(st2))
		return 1
		
   


k = sys.argv

if len(k) >=2:
	with open(k[1],'r') as fl:
		data_w = fl.read()
	
	words = data_w.split()

	ct = 0

	for i in range(len(words)):
		for j in range(i+1,len(words)):
			ct += anangram_chk(words[i],words[j])

	print(ct)