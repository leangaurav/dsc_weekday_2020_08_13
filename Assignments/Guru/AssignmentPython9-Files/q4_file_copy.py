#Q4 WAP to read file and write a content into a new file
import os.path
import sys

try:
    source_file = input("Enter a file name to be copied : ")
  
    # check if the file exists
 
    dot_index =  source_file.rfind(".") # get the index position of . 
    target_file = source_file[:dot_index] + "_copy" + source_file[dot_index:]
    print("copying {} to {}".format(source_file,target_file))

    with open(source_file,'r') as s_file:
        print(source_file)
        with open(target_file,'w') as t_file:
             t_file.write(s_file.read())
            
except FileNotFoundError:
    print("File not found!!")



    