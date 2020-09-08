import sys

k = sys.argv

if len(k) >=3:
	with open(k[1],'r') as fl:
		data1 = fl.read()
	with open(k[2],'r') as fl:
		data2 = fl.read()
	if data1 == data2:
		print(True)
	else:
		print(False)
else:
	print('Enter 2 files to compare')