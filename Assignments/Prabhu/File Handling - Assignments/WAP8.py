#  Write a script called diff.py that take two file names as arguments 
# and checks if the content of both the files is same and prints true or false. 

import sys

src_file=open(sys.argv[1],"r")
tgt_file=open(sys.argv[2],"r")

src_content=src_file.read()
tgt_content=tgt_file.read()

if src_content==tgt_content :
	print("True")
else :
	print("False")
	

src_file.close()
tgt_file.close()