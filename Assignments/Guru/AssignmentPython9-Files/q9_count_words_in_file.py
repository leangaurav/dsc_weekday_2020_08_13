import sys
import string

if len(sys.argv) == 2:
    source_file = sys.argv[1]
else:
    source_file = input("Enter a file name : ")

    
with open(source_file,'r') as s_file:
    file_content = s_file.read()
#     print(file_content)
    words = file_content.split()
    
print("Numer of words in file {} is {}".format(source_file,len(words)))
    