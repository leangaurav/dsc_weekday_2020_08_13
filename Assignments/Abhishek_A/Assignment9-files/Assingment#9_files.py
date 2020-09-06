#Write a program in python that stores alphabets from a to z in a text file.
import string
f = open("answer#1.txt", 'w') #write mode
a=[]
for i in string.ascii_lowercase:
	a.append(i)
print(a, file=f)

f.close()

#Write a program to read itself and print on the screen (Use Command Line Arguments).
import string
f = open("q1.py", 'r') #read mode
f1 = open("Answer#2.txt", 'w') #write mode
f1.write(f.read())
f1.close()

#Predict output of the following piece of code:
f3 = open("answer3.1.txt",'w')
f3.write('Line with some characters')
f3.close()

f = open("answer3.1.txt",'r')
print(f.tell())
print(f.read(4))
print(f.tell())

#Write a program to read a file and copy it into a new file.

f = open("q1.py", 'r') #read mode
f1 = open("Answer#4.txt", 'w') #write mode
f1.write(f.read())
f1.close()

#Write a program to read a file and copy the contents to a new file such that the case gets reversed. i.e. upper case becomes #lower case and vice versa.

f6 = open("q1.py", 'r') #read mode
f5 = open("Answer#5.txt", 'a') #write mode
for i in f6.read():
	if i.isupper() == 'TRUE':
		f5.write(i.lower())
	else:
		f5.write(i.upper())
f5.close()

#Write a program that take a file name as command line argument, opens it and then counts
#number of space characters in that file.

filename = input('Enter filename: ')
f8 = open("Answer#6.txt", 'w') 
f7 =open(filename,'r')
cnt = 0
for i in f7.read():
	if i == ' ':
		cnt+=1
f8.write(str(cnt))
f8.close()

