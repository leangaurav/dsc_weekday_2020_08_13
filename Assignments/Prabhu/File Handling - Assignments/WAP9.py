#  WAP to count the number of words in a file. 

src_file=open("random.txt","r")
content=src_file.read()

print("No. of. words in the file are ", len(content.split()))

src_file.close()