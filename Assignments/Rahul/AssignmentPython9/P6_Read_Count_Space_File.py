# 6. Write a program that take a file name as command line argument, opens it and then counts number of space characters in that file
import sys

if len(sys.argv) >=2:
	file_name_src=sys.argv[1]
	try:
		with open(file_name_src,'r') as f_src:
			cnt=0
			while True:
				next_char=f_src.read(1)
				if next_char =='':
					break
				elif next_char==' ':
					cnt+=1
		print(f"The total number of spaces in given file is : {cnt}")
	except FileNotFoundError:
		print("Please enter a valid file to copy")	
else:
	print("Please enter file name to be copied")