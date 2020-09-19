import sys

lst=[]  
for file in sys.argv[1:]:
    with open(file,"r") as file1:
        strfile=file1.readlines()
        lst.append(strfile)

print(lst[0],lst[1])
if len(lst) > 1 and lst[0] == lst[1]:
    print("File content is same")
else:
    print("File content is not same")