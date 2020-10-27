#Q8 Write a script called diff.py that take two file names as arguments and checks if the content of both the files is same and #prints true or false.

import sys
# print(sys.argv)
    
try:
    if len(sys.argv) == 3:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
#         print(file1,file2)
    else:
        print("Enter 2 file names to compare")
    
    with open(file1,'r') as f1:
        f1_content = f1.read()
#         print(f1_content)
        with open(file2,'r') as f2:
            f2_content = f2.read()
#             print(f2_content)
            if f1_content == f2_content:
                flag = 'True'
            else:
                flag = 'False'
    

    print(flag)
#     if flag:
#         print("file {} and file {} are the same".format(file1,file2))
#     else:
#         print("file {} and file {} are not the same".format(file1,file2))       


except Exception as err:
    print(err)
    
    
    
# import sys
# file_names=sys.argv[1:]
# try:
#     with open(file_names[0],'r') as f1:
#         with open(file_names[1],'r') as f2:
#             print(f1.read()==f2.read())
# except Exception as err:
#     print(err)