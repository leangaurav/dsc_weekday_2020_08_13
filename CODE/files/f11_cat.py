import sys

file_name = sys.argv[0]
if len(sys.argv) == 2:
    file_name = sys.argv[1]

try:
    with open(file_name, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found!!")

"""
import sys
self_name = sys.argv[0]
self_name1 = sys.argv[1] # index error ????

if len(self_name1>0):
	print(self_name1)
else:
    print(self_name)

"""