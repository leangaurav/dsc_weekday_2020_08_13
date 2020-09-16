# 7. Modify the above program to count the occurrence of each symbol i.e. count of alphabet ‘a’, count of spaces, count of commas and so forth
import sys

if len(sys.argv) >=2:
	file_name_src=sys.argv[1]
	try:
		with open(file_name_src,'r') as f_src:
			d={}
			while True:
				i=f_src.read(1)
				if i!='':
					if i in d:
						d[i]=d.get(i,0)+1
					else:
						d[i]=1
				else:
					break
		print(f"The occurance of each character is {d}")
	except FileNotFoundError:
		print("Please enter a valid file to copy")	
else:
	print("Please enter file name to be copied")