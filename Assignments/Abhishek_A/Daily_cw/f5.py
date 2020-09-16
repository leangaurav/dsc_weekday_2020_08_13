with open("status1.txt",'r') as f:
	s=f.read(4)
	while len(s)>0:
		print(s)
	f.close()