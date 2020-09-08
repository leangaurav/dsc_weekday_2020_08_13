import sys

k = sys.argv

if len(k)==2:
	ct = 0
	with open(k[1],'r') as fl:
		data = fl.read()
	for i in data:
		if i == ' ':
			ct += 1
	
	print('Count of spaces in file {} - {} '.format(k[1],ct))
	#print(repr(data))