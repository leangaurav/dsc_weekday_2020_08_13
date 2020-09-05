f = open("numbers.txt", 'w') #write mode
for i in range(10):
	print(i,sep='\n', file=f)
f.close()