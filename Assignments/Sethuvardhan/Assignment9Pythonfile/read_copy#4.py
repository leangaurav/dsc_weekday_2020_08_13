import sys

k = sys.argv

if len(k)==2:
	with open(k[1],'r') as fl:
		ind = k[1].rfind('.')
		f_name = k[1][:ind] + '_copy' + k[1][ind:]
		with open(f_name,'w') as f2:
			f2.write(fl.read())
else:
	with open(k[0],'r') as fl:
		ind = k[0].rfind('.')
		f_name = k[0][:ind] + '_copy' + k[0][ind:]
		with open(f_name,'w') as f2:
			f2.write(fl.read())

