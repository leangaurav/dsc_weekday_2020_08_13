#Q3 WAP to predict the output

f = open('file','w')                  # creates a file with name 'file'
f.write('Have a great day')           # writes into that file
f.close()

f = open('file','r')                  # opens the file for reading
print(f.tell())                       # prints the position of the file
print(f.read(4))                      # reads 4 bytes from the file
print(f.tell())