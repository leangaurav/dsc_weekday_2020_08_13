# 5. Write a program to read a file and copy the contents to a new file such that the case gets reversed. i.e. upper case becomes lower case and vice versa
import sys

if len(sys.argv) >=2:
	file_name_src=sys.argv[1]
	idx_file=file_name_src.find(".")
	file_name_tgt=file_name_src[:idx_file]+"_copy"+file_name_src[idx_file:]
	try:
		with open(file_name_src,'r') as f_src:
			with open(file_name_tgt,'w') as f_tgt:
				content_src=f_src.read()
				f_tgt.write(content_src.swapcase())
		print("Below is copied file output")
		with open(file_name_tgt,'r') as f_tgt:
			print(f_tgt.read())
	except FileNotFoundError:
		print("Please enter a valid file to copy")	
else:
	print("Please enter file name to be copied")