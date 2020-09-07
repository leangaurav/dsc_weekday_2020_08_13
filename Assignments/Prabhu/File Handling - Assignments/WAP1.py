#Write a program in python that stores alphabets from a to z in a text file. 

file=open("alpha.txt","w")

for i in range(26):
    file.write(chr(65+i))

file.close()