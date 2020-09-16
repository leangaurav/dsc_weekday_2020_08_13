import sys

name = sys.argv[1]

f = open(name,'r')
content = f.read()

Count = 0

for i in content:
    if i.isspace() == True:
        Count = Count + 1

print("The number of Counts :", Count)


f.close()