#  Write a program to read a file and copy it into a new file. 

src_file=open("alpha.txt","r")
content=src_file.read()
tgt_file=open("alpha1.txt","w")
tgt_file.write(content)

src_file.close()
tgt_file.close()

