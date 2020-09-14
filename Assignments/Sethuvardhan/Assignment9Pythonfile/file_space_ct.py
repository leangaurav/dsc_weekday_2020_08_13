import sys

k = sys.argv

if len(k) >= 2:
	with open(k[1],'r') as fl:
		data = fl.read()
	sp_ct = 0
	print(repr(data))
	for k in data:
		if k == ' ':
			sp_ct += 1
	print('Number of spaces in file : {}'.format(sp_ct))
else:
	print('File name not entered')