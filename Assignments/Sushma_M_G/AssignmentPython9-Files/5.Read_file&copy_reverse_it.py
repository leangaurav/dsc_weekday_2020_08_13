f = open("file.txt","r")
content = f.read()

f1 = open("copy_of_file.txt","w")

for i in content:
    if i.islower() == True:
        f1.write(i.upper())
    else:
        f1.write(i.lower())
        
#f1.write(content)

f.close()
f1.close()