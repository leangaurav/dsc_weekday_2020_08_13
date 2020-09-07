#  Update the above program to count the number of palindromes present in the file. 

src_file=open("random.txt","r")
content=src_file.read()
words = content.split()

cnt=0
for word in words :
    if word==word[::-1] :
            cnt+=1

print("No. of. Palindromes in the file are ", cnt)

src_file.close()