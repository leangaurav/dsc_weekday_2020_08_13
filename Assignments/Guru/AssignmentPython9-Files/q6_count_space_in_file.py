# Q6 WAP to take the file name at command line argument and count number of space characters in the file 

import sys

if len(sys.argv) == 2:
    source_file = sys.argv[1]
else:
    print("File name not given")
    
print(source_file)
count = 0 
with open(source_file,'r') as s_file:
    for line in s_file.readlines():
        print(line)
        for i in line:
             if(i.isspace()):
                count=count+1
    print("The number of space in {} is {}".format(source_file,count)) 
                
               
