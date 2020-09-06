# 2. Write a program to read itself and print on the screen (Use Command Line Arguments)

import sys

file_name=sys.argv[0]

with open(file_name,'r') as src_file:
	print(src_file.read())