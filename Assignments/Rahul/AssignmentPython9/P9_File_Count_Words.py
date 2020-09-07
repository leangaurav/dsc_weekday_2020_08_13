# 9. WAP to count the number of words in a file
import sys

if len(sys.argv) >=2:
	file_name_src=sys.argv[1]
	try:
		with open(file_name_src,'r') as f_src:
			src_content=f_src.read()
			file_len=len(src_content.split())
		print(f"The number of words in file is  {file_len}")
	except FileNotFoundError:
		print("Please enter a valid file to copy")	
else:
	print("Please enter file name to be copied")