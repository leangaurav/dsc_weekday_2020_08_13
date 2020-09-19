#Q1 Write a program in python that stores the alphabets from a to z in the file

file_name = input("Enter a File name: ")
import string
with open(file_name, 'w') as file:
    file.write(string.ascii_lowercase)
    
# with open("Q1.txt", 'w') as f:
#     f.write(",".join(list(map(lambda x: chr(x), range(65,91)))))
    
