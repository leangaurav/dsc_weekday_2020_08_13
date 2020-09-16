import sys

name1 = sys.argv[1]
name2 = sys.argv[2]

f1 = open(name1,'r')
f2 = open(name2, 'r')

content1 = f1.read()
content2 = f2.read()

if content1 == content2:
    print(True)
else:
    print(False)
    
f1.close()
f2.close()