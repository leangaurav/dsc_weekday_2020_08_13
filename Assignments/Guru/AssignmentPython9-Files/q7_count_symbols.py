#Q7 WAP to take the file name at command line argument and count the occurrence of each symbol i.e count of 'a', count of #spaces, count of commas,etc.

import sys

if len(sys.argv) == 2:
    source_file = sys.argv[1]
else:
    source_file = input("Enter a source file :")

unique_char = []
with open(source_file,'r') as s_file:
    s = s_file.read()
    for c in s:
        if c not in unique_char:
            unique_char.append(c)
    print(unique_char)
 

count = []
with open(source_file,'r') as s_file:
    s = s_file.read()
    for c in unique_char:
        count.append((c, s.count(c)))

for e in count:
    print(e)

# s = string.ascii_letters + " " + string.digits
# #print(s)

# def char_freq(s):
#     s1=[]
# # finds out unique characters
#     for c in s:
#         if c not in s1:
#             s1.append(c)
# #    print(s1)
#     count=[]
#     for i in s1:
#         count.append((i, s.count(i)))
#     return count


#--

# import sys
# file_name=sys.argv[1:]
# try:
#     with open(file_name[0],'r') as f:
#         content=f.read()
#         res={}
#         for i in content:
#             res[i]=1+res.get(i,0)
#         print(res)
# except Exception as err:
#     print(err)
