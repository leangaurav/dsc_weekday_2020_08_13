f = open("file",'w')
f.write('line with some characters')
f.close()

f = open("file",'r')
print(f.tell()) # tells where is the cursor
print(f.read(4)) # prints first 4 characters of the file
print(f.tell()) 
