# 8. Write a script called diff.py that take two file names as arguments and checks if the content of both the files is same and prints true or false
import sys

if len(sys.argv) >=3:
	file_name1=sys.argv[1]
	file_name2=sys.argv[2]
	try:
		with open(file_name1,'r') as f1:
			with open(file_name2,'r') as f2:
				flag=0
				while True:
					i1=f1.read(1)
					i2=f2.read(1)
					if i1=='' or i2=='':
						break
					elif i1!=i2:
						flag=1
			if flag==0:
				print("The given files are same")
			else:
				print("The given files are different")
	except FileNotFoundError:
		print("Please enter a valid file to copy")	
else:
	print("Please enter file name to be compared")