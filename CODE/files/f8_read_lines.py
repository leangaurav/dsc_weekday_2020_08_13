# read entire file read()
# read fixed bytes read(n)
# read line by line readline()
# read all lines in a list readlines()


print("\n\n READ")
with open("lines.txt", "r") as file:
    print(file.read())


print("\n\n READLINE")
with open("lines.txt", "r") as file:
    
    while True:
        s = file.readline()
        if not s:
            break
        print(s, end='')
        

print("\n\n for")
with open("lines.txt", "r") as file:
    for s in file: # automatically reads line by line
        print(s, end='')
        
        
print("\n\n readlines")
with open("lines.txt", "r") as file:
    print(file.readlines())