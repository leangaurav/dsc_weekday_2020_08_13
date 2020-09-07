# Write a program to read a file and copy the contents to a new file such that the case gets reversed. 
# i.e. upper case becomes lower case and vice versa. 

src_file=open("alpha1.txt","r")
content=src_file.read()
tgt_file=open("alpha2.txt","w")

for i in content :
	if i.isupper():
		tgt_file.write(i.lower())
	else:
		tgt_file.write(i.upper())

src_file.close()
tgt_file.close()