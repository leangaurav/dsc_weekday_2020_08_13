with open("status.txt",'w') as f:
	for i in range(10):
		print(i,sep='\n', file=f)
	f.close()
print("status",f.closed)
