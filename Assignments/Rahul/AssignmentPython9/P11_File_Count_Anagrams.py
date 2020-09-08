# 11. Update the program again to count and print number of anagrams in the file
import sys

if len(sys.argv) >=2:
	file_name_src=sys.argv[1]
	try:
		with open(file_name_src,'r') as f_src:
			input_src=f_src.read().split()
			i_src=[]
			i_tgt={}
			for j in input_src:
				d=list(j.lower())
				d.sort()
				i_src.append(''.join(d))
			for k in i_src:
				cnt=i_src.count(k)
				if cnt==2:
					i_tgt[k]=cnt
			list_anag=i_tgt.keys()
			print(f"Following are the list of anagrams : {list(list_anag)}")
	except FileNotFoundError:
		print("Please enter a valid file to copy")	
else:
	print("Please enter file name to be copied")