#  Update the above program to count the number of palindromes present in the file. 

import sys
src_file=open(sys.argv[1],"r")
content=src_file.read()

cnt=0
for ch in content :
    if ch.isspace() :
        cnt+=1

print("No. of. spaces in the file are ", cnt)

src_file.close()