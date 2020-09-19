#Q5 WAP to read file and write a content into a new file, and change the case Upper->Lower and Lower->Upper
import string
source_file = input("Enter a file name: ")
dot_index = source_file.rfind(".")
target_file = source_file[:dot_index] + "case_reversed" + source_file[dot_index:]

with open(source_file,'r') as s_file:
#     for word in s_file.read():       # reads each character 
#         print(word)
#       for line in s_file.readlines():       # reads each line and prints each line 
#         print(line,type(line))
    for line in s_file.readlines():       # reads each line and prints each line 
        for word in line.split():
            word = word.swapcase()
            with open(target_file,'a') as t_file:
                 print(word,end=" ",file=t_file)
        with open(target_file,'a') as t_file: 
             print('\n',file=t_file)