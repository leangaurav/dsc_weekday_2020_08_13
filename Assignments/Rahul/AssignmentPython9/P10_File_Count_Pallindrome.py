# 10. Update the above program to count the number of palindromes present in the file

import sys

if len(sys.argv) >=2:
	file_name_src=sys.argv[1]
	try:
		with open(file_name_src,'r') as f_src:
			src_content=f_src.read()
			a=src_content.split()
			cnt=0
			for i in a:
				elements=i.upper()
				if elements==elements[::-1]:
					cnt+=1
		print(f"The number of words in file is  {cnt}")
	except FileNotFoundError:
		print("Please enter a valid file to copy")	
else:
	print("Please enter file name to be copied")