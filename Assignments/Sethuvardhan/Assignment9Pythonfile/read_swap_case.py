import sys

k = sys.argv

if len(k)==2:
	with open(k[1],'r') as fl:
		data = fl.read()
		ind = k[1].rfind('.')
		f_name = k[1][:ind] + '_copy_swapped' + k[1][ind:]
		with open(f_name,'w') as f2:
			for k in data:
				f2.write(k.swapcase())

