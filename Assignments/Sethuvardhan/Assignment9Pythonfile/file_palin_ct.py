import sys
import re
import string

k = sys.argv

if len(k) >=2:
	with open(k[1],'r') as fl:
		data_w = fl.read()
	#words = re.split(string.whitespace,data_w)
	words = data_w.split()
	print(words)
	words = list(filter(lambda x:True if x==x[::-1] else False,words))
	print(words,len(words))
else:
	print('Enter input file name')
