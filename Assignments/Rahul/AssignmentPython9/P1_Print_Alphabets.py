# 1. Write a program in python that stores alphabets from a to z in a text file
import string
with open("P1_Print_Alphabet_Out.txt","w") as f:
	for i in string.ascii_lowercase:
		print(i,file=f)

	